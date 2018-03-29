# coding=utf-8

"""

boss-API接口返回信息的data部分的校验
# 注意SQL语句中字符串类型用''表示

__author__ = 'liwenxuan'

"""

import time
from lib.interface.boss.time_handler import get_date_list_by_date
from lib.database.mysql_db_v2 import MysqlDB
from lib.database.postgresql_db import PostgresqlDB
from lib.decorator.trace import *

from lib.interface.boss.environment_constant import BOSS_POSTGRESQL_HOST, BOSS_MYSQL_HOST


# 内部接口与上游接口通用
@print_trace
def get_activity_online_info_data(customer_id, start_time, end_time):
    """
    Panel对接接口 get_activity_online_info接口及上游接口activity_online_info接口应该返回的data, data结构如下:
    "data": {*start_time: 0}
    """
    sql = "select info from boss_activity_online where timestamp >= {0} and timestamp < {1} and \
prefix = '{2}' order by timestamp desc limit 1"

    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    if customer_id != "all":
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix as p inner join crm_customer_info as i \
on p.customer = i.id where i.number = '{0}'".format(customer_id)).one_by_one()
    else:
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix").one_by_one()
    del pg_db

    data = {}
    if len(prefix_list) == 0:
        return data
    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    for timestamp in range(start_time, end_time, 3600000):
        online_info_list = []
        for prefix in prefix_list:
            one_online_info = mysql_db.execute(sql.format(timestamp, timestamp + 3600000, prefix)).one_by_one()
            if len(one_online_info) == 1:
                online_info_list.append(one_online_info[0])
        online = 0
        for online_info in online_info_list:
            online_info = eval(online_info)  # 如 {'provinces': {}, 'isps': {}, 'natTypes': {}, 'versions': {}}
            online_province = online_isp = online_nat_type = online_version = 0
            for v in online_info["provinces"].values():
                online_province += v
            for v in online_info["isps"].values():
                online_isp += v
            for v in online_info["natTypes"].values():
                online_nat_type += v
            for v in online_info["versions"].values():
                online_version += v
            assert online_province == online_isp == online_nat_type == online_version
            online += online_province
        data[str(timestamp)] = int(online)
    del mysql_db

    return data


# 内部接口
@print_trace
def get_customer_info_data(prefix):
    """
    计费模块 get_customer_info接口应该返回的data, data结构如下
    data = {customer_id: {"prefixes": [prefix1, prefix2, ...],
                          "table_info": {"upload_log": table_name, "download_log": table_name},
                          "blockinfo": {
                              "*prefix": {
                                  "*upload/download": {"current": {}, "ts_into_effect": 1, "previous": {}}}},
                          "customer_id": customer_id}}
    """
    data = {}
    db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)

    if prefix == "all":
        customer_index_list = db.execute("select id from crm_customer_info order by id").one_by_one()
    else:
        customer_index_list = db.execute("select customer from crm_customer_prefix where prefix = '{0}'".format(prefix)).one_by_one()

    for customer_index in customer_index_list:
        customer_id = db.execute("select number from crm_customer_info where id = {0}".format(customer_index)).only_one()
        prefix_list = db.execute("select prefix from crm_customer_prefix where customer = {0} order by id".format(customer_index)).one_by_one()

        table_info_list = db.execute("select table_name from crm_customer_tableinfo where customer = {0} order by id".format(customer_index)).one_by_one()
        if len(table_info_list) == 2:
            table_info = {"upload_log": table_info_list[0], "download_log": table_info_list[1]}
        elif len(table_info_list) == 0:
            table_info = {}
        else:
            raise ValueError

        block_info = {}
        for one_prefix in prefix_list:
            prefix_dict = {}
            customer_name = db.execute("select name from crm_customer_info where id = {0}".format(customer_index)).only_one().decode("utf-8")
            for category in ["upload", "download"]:
                current = db.execute("select b.category as category, b.customer as customer, p.prefix as prefix, start_time, interval, to_bill \
from crm_customer_blockinfo as b inner join crm_customer_prefix as p on b.prefix = p.id \
where p.prefix = '{0}' and b.category = '{1}' order by b.id".format(one_prefix, category)).to_dict()
                if len(current) == 0:
                    continue
                ts, previous_str = db.execute("select ts_into_effect, previous_info from crm_customer_blockinfo as b \
inner join crm_customer_prefix as p on b.prefix = p.id \
where p.prefix = '{0}' and b.category = '{1}' order by b.id".format(one_prefix, category)).to_cols()
                for i in range(len(current)):
                    current[i]["customer"] = customer_name
                    if ts[i] == 0 or ts[i] is None:
                        ts_into_effect = None
                    else:
                        ts_into_effect = ts[i]
                    if previous_str[i] is not None:
                        previous = eval(previous_str[i])
                        previous["prefix"] = one_prefix
                    else:
                        previous = None
                    prefix_dict[category] = {"current": current[i], "ts_into_effect": ts_into_effect, "previous": previous}
                    block_info[one_prefix] = prefix_dict

        data[customer_id] = {"prefixes": prefix_list, "table_info": table_info, "blockinfo": block_info, "customer_id": customer_id}

    del db
    return data


@print_trace
def get_billing_rule_data(prefix, category):
    """
    计费模块 get_billing_rule接口应该返回的data, data结构如下
    "data": {"category": "flow", "amount_unit": "GB" or "MB" or "KB", "billing_strategy": "\u57fa\u7840\u8ba1\u8d39",
             "params": "{\"price\": 0.95}", "monetary_unit": "CNY"}
    """
    db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)

    customer_index = db.execute("select customer from crm_customer_prefix where prefix = '{0}'".format(prefix)).only_one()
    data_list = db.execute("select br.category as category, amount_unit, billing_strategy, params, monetary_unit \
from crm_customer_billingrules as br inner join crm_customer_contractinfo as ci on br.contract = ci.id \
where br.category = 'flow' and ci.customer = {0} and ci.category = '{1}'".format(customer_index, category)).to_dict()
    if len(data_list) == 1:
        data = data_list[0]
    else:
        print data_list
        raise ValueError
    billing_strategy = db.execute("select name from crm_customer_billingstrategy where id = {0}".format(data["billing_strategy"])).only_one().decode("utf-8")

    del db
    data["billing_strategy"] = billing_strategy

    return data


@print_trace
def get_qos_startup_data(customer_id, start_time, end_time):
    """
    Panel对接接口 get_qos_startup接口应该返回的data, data结构如下:
    "data": {*start_time: {"middle": 0, "long": 0, "less": 0}}
    """
    sql = "select count(*) from qos_startup where "

    if customer_id != "all":
        pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
        customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix where customer = {0}".format(customer_index)).one_by_one()
        del pg_db

        if len(prefix_list) == 0:
            sql += "prefix = 'Not Exist' and "
        elif len(prefix_list) == 1:
            sql += "prefix = '{0}' and ".format(prefix_list[0])
        else:
            sql += "prefix in {0} and ".format(tuple(prefix_list))

    data = {}
    sql_less = sql + "duration > 0 and duration < 1000 and timestamp >= {0} and timestamp < {1}"
    sql_middle = sql + "duration >= 1000 and duration < 3000 and timestamp >= {0} and timestamp < {1}"
    sql_long = sql + "duration >= 3000 and timestamp >= {0} and timestamp < {1}"

    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    for timestamp in range(start_time, end_time, 300000):
        less = mysql_db.execute(sql_less.format(timestamp, timestamp + 300000)).only_one()
        middle = mysql_db.execute(sql_middle.format(timestamp, timestamp + 300000)).only_one()
        long = mysql_db.execute(sql_long.format(timestamp, timestamp + 300000)).only_one()
        data[str(timestamp)] = {"less": int(less), "middle": int(middle), "long": int(long)}
    del mysql_db

    return data


@print_trace
def get_qos_buffer_data(customer_id, start_time, end_time):
    """
    Panel对接接口 get_qos_buffer接口应该返回的data, data结构如下:
    "data": {*start_time: {"middle": 0, "majority": 0, "less": 0, "zero": 0}}
    """
    sql = "select count(*) from qos_buffer where "

    if customer_id != "all":
        pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
        customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix where customer = {0}".format(customer_index)).one_by_one()
        del pg_db

        if len(prefix_list) == 0:
            sql += "prefix = 'Not Exist' and "
        elif len(prefix_list) == 1:
            sql += "prefix = '{0}' and ".format(prefix_list[0])
        else:
            sql += "prefix in {0} and ".format(tuple(prefix_list))

    data = {}
    sql_zero = sql + "buffering_count = 0 and timestamp >= {0} and timestamp < {1}"
    sql_less = sql + "buffering_count = 1 and timestamp >= {0} and timestamp < {1}"
    sql_middle = sql + "buffering_count in (2, 3) and timestamp >= {0} and timestamp < {1}"
    sql_majority = sql + "buffering_count > 3 and timestamp >= {0} and timestamp < {1}"

    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    for timestamp in range(start_time, end_time, 300000):
        zero = mysql_db.execute(sql_zero.format(timestamp, timestamp + 300000)).only_one()
        less = mysql_db.execute(sql_less.format(timestamp, timestamp + 300000)).only_one()
        middle = mysql_db.execute(sql_middle.format(timestamp, timestamp + 300000)).only_one()
        majority = mysql_db.execute(sql_majority.format(timestamp, timestamp + 300000)).only_one()
        data[str(timestamp)] = {"zero": int(zero), "less": int(less), "middle": int(middle), "majority": int(majority)}
    del mysql_db

    return data


@print_trace
def get_customers_data():
    """
    Panel对接接口 get_customers接口应该返回的data, data结构如下:
    "data": [{"number": customer_id, "name": customer_name}, {}, ...]
    """
    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    data = pg_db.execute("select number, name, need_bills from crm_customer_info order by id").to_dict()
    del pg_db

    for customer_info in data:
        customer_info["name"] = str(customer_info["name"]).decode("utf-8")

    return data


@print_trace
def get_activity_number_data(customer_id):
    """
    Panel对接接口 get_activity_number接口应该返回的data, data结构如下:
    "data": {"active": 0, "online": 0}
    """
    millisecond_now = int(time.time()) * 1000
    today = time.strftime('%Y-%m-%d', time.localtime())
    sql_active = "select count(*) from boss_activity where report_date = '{0}' and prefix = '{1}'"
    sql_online = "select info from boss_activity_online where timestamp > {0} and prefix = '{1}' order by timestamp desc limit 1"

    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    if customer_id != "all":
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix as p inner join crm_customer_info as i \
on p.customer = i.id where i.number = '{0}'".format(customer_id)).one_by_one()
    else:
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix").one_by_one()
    del pg_db

    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    active = 0
    online_info_list = []
    for prefix in prefix_list:
        one_active = mysql_db.execute(sql_active.format(today, prefix)).only_one()
        active += one_active
        one_online_info = mysql_db.execute(sql_online.format(millisecond_now - 3600000, prefix)).one_by_one()
        if len(one_online_info) == 1:
            online_info_list.append(one_online_info[0])
    del mysql_db

    online = 0
    for online_info in online_info_list:
        online_info = eval(online_info)  # 如 {'provinces': {}, 'isps': {}, 'natTypes': {}, 'versions': {}}
        online_province = online_isp = online_nat_type = online_version = 0
        for v in online_info["provinces"].values():
            online_province += v
        for v in online_info["isps"].values():
            online_isp += v
        for v in online_info["natTypes"].values():
            online_nat_type += v
        for v in online_info["versions"].values():
            online_version += v
        assert online_province == online_isp == online_nat_type == online_version
        online += online_province

    data = {"active": int(active), "online": int(online)}

    return data


@print_trace
def get_activity_info_data(customer_id, start_time, end_time):
    """
    Panel对接接口 get_activity_info接口应该返回的data, data结构如下:
    "data": {*start_time: 0}
    """
    sql = "select ifnull(sum(daily), 0) from boss_daily_activities where bill_date = '{0}' and prefix = '{1}'"

    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    if customer_id != "all":
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix as p inner join crm_customer_info as i \
on p.customer = i.id where i.number = '{0}'".format(customer_id)).one_by_one()
    else:
        prefix_list = pg_db.execute("select prefix from crm_customer_prefix").one_by_one()
    del pg_db

    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    data = {}
    for timestamp in range(start_time, end_time, 86400000):
        active = 0
        date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
        for prefix in prefix_list:
            one_active = mysql_db.execute(sql.format(date, prefix)).only_one()
            active += one_active
        data[str(timestamp)] = int(active)
    del mysql_db

    return data


@print_trace
def get_traffic_info_data(customer_id, start_time, end_time, step):
    """
    Panel对接接口 get_traffic_info接口应该返回的data, data结构如下
    "data": {"download": {*start_time: {"app": 0, "cdn": 0, "p2p": 0, "sum": cdn+p2p}}, "upload": {*start_time: {"upload": 0}}}
    """
    # 分api_block
    if step == "day":
        interval = 86400000
    elif step == "hour":
        interval = 3600000
    elif step == "minute":
        interval = 300000
    else:
        raise ValueError

    data = {"download": {}, "upload": {}}
    db = MysqlDB(host=BOSS_MYSQL_HOST)
    # step为"day"与step为"hour"或"minute"时, 查询的表不同, 表结构也有不同
    for timestamp in range(start_time, end_time, interval):
        sql_download = "select ifnull(sum(app), 0), ifnull(sum(cdn), 0), ifnull(sum(p2p), 0) "
        sql_upload = "select ifnull(sum(upload), 0) "

        if step == "day":
            sql_download += "from boss_daily_download where customer_id = '{0}' and report_date = '{1}'"
            sql_upload += "from boss_daily_upload where customer_id = '{0}' and  report_date = '{1}'"
            date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
            app, cdn, p2p = db.execute(sql_download.format(customer_id, date)).one_by_one()
            upload = db.execute(sql_upload.format(customer_id, date)).only_one()
        else:
            sql_download += "from download_log_{0} where timestamp >= {1} and timestamp < {2}"
            sql_upload += "from upload_log_{0} where timestamp >= {1} and timestamp < {2}"
            try:
                db.execute("select * from download_log_{0} limit 1".format(customer_id))
                db.execute("select * from upload_log_{0} limit 1".format(customer_id))
            except:
                return data
            app, cdn, p2p = db.execute(sql_download.format(customer_id, timestamp, timestamp + interval)).one_by_one()
            upload = db.execute(sql_upload.format(customer_id, timestamp, timestamp + interval)).only_one()

        data["download"][str(timestamp)] = {"app": int(app), "cdn": int(cdn), "p2p": int(p2p), "sum": int(cdn + p2p)}
        data["upload"][str(timestamp)] = {"upload": int(upload)}
    del db

    return data


@print_trace
def get_bandwidth_info_data(customer_id, start_time, end_time, step):
    """
    Panel对接接口 get_bandwidth_info接口应该返回的data, data结构如下
    "data": {"download": {*start_time: {"app": 0.00, "cdn": 0.00, "p2p": 0.00, "sum": cdn+p2p}},
             "upload": {*start_time: {"upload": 0.00}}}
    """
    # 分api_block
    if step == "day":
        interval = 86400000
    elif step == "hour":
        interval = 3600000
    elif step == "minute":
        interval = 300000
    else:
        raise ValueError

    data = {"download": {}, "upload": {}}
    db = MysqlDB(host=BOSS_MYSQL_HOST)
    # step为"day"与step为"hour"或"minute"时, 查询的表不同, 表结构也有不同
    for timestamp in range(start_time, end_time, interval):
        sql_download = "select ifnull(sum(app), 0), ifnull(sum(cdn), 0), ifnull(sum(p2p), 0) "
        sql_upload = "select ifnull(sum(upload), 0) "

        if step == "day":
            sql_download += "from boss_daily_download where customer_id = '{0}' and report_date = '{1}'"
            sql_upload += "from boss_daily_upload where customer_id = '{0}' and  report_date = '{1}'"
            date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
            app, cdn, p2p = db.execute(sql_download.format(customer_id, date)).one_by_one()
            upload = db.execute(sql_upload.format(customer_id, date)).only_one()
        else:
            sql_download += "from download_log_{0} where timestamp >= {1} and timestamp < {2}"
            sql_upload += "from upload_log_{0} where timestamp >= {1} and timestamp < {2}"
            try:
                db.execute("select * from download_log_{0} limit 1".format(customer_id))
                db.execute("select * from upload_log_{0} limit 1".format(customer_id))
            except:
                return data
            app, cdn, p2p = db.execute(sql_download.format(customer_id, timestamp, timestamp + interval)).one_by_one()
            upload = db.execute(sql_upload.format(customer_id, timestamp, timestamp + interval)).only_one()

        app = round(app*8/(interval/1000), 2)
        cdn = round(cdn*8/(interval/1000), 2)
        p2p = round(p2p*8/(interval/1000), 2)
        sum = round((cdn + p2p)*8/(interval/1000), 2)
        upload = round(upload*8/(interval/1000), 2)
        data["download"][str(timestamp)] = {"app": app, "cdn": cdn, "p2p": p2p, "sum": sum}
        data["upload"][str(timestamp)] = {"upload": upload}
    del db

    return data


# 下游客户接口
@print_trace
def down_traffic_total_data(customer_id, start_time, end_time, domain=None):
    """
    下游客户 down_traffic_total接口应该返回的data, data结构如下
    "data": {*domain: {"time": 1489507200000, "app_total_ratio": app/(cdn+p2p), "app": 0, "cdn": 0, "p2p": 0}}
    """
    if domain is None:
        pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
        domains = pg_db.execute("select domain_name from crm_customer_domain as d inner join crm_customer_info as i \
on d.customer = i.id where i.number = '{0}'".format(customer_id)).one_by_one()
        del pg_db
    else:
        domains = [domain]

    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    data = {}
    for dns in domains:
        app, cdn, p2p = mysql_db.execute("select ifnull(sum(app), 0), ifnull(sum(cdn), 0), ifnull(sum(p2p), 0) \
from download_log_{0} where timestamp >= {1} and timestamp < {2} and DNS = '{3}'"
                                   .format(customer_id, start_time, end_time, dns)).one_by_one()
        if (cdn + p2p) != 0:
            app_total_ratio = round(app / (cdn + p2p), 4)
        else:
            app_total_ratio = 0.0
        data[dns] = {"time": start_time, "app_total_ratio": app_total_ratio, "app": int(app), "cdn": int(cdn), "p2p": int(p2p)}
    del mysql_db

    return data


@print_trace
def down_traffic_info_data(customer_id, start_time, end_time, step, domain=None):
    """
    下游客户 down_traffic_info接口应该返回的data, data结构如下
    "data": {*start_time: {"app": 0, "cdn": 0, "p2p": 0, "sum": cdn+p2p}}
    """
    # 分api_block
    if step == "day":
        interval = 86400000
    elif step == "hour":
        interval = 3600000
    elif step == "minute":
        interval = 300000
    else:
        raise ValueError

    data = {}
    db = MysqlDB(host=BOSS_MYSQL_HOST)
    # step为"day"与step为"hour"或"minute"时, 查询的表不同, 表结构也有不同
    for timestamp in range(start_time, end_time, interval):
        sql_download = "select ifnull(sum(app), 0), ifnull(sum(cdn), 0), ifnull(sum(p2p), 0) "
        if step == "day":
            sql_download += "from boss_daily_download where customer_id = '{0}' and report_date = '{1}' "
            if domain is not None:
                sql_download += "and DNS = '{0}'".format(domain)
            date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
            app, cdn, p2p = db.execute(sql_download.format(customer_id, date)).one_by_one()
        else:
            sql_download += "from download_log_{0} where timestamp >= {1} and timestamp < {2} "
            if domain is not None:
                sql_download += "and DNS = '{0}'".format(domain)
            app, cdn, p2p = db.execute(sql_download.format(customer_id, timestamp, timestamp + interval)).one_by_one()
        data[str(timestamp)] = {"app": int(app), "cdn": int(cdn), "p2p": int(p2p), "sum": int(cdn + p2p)}
    del db

    return data


@print_trace
def down_bandwidth_info_data(customer_id, start_time, end_time, step, domain=None):
    """
    下游客户 down_bandwidth_info接口应该返回的data, data结构如下
    "data": {*start_time: {"app": 0, "cdn": 0, "p2p": 0, "sum": cdn+p2p}}
    """
    # 分api_block
    if step == "day":
        interval = 86400000
    elif step == "hour":
        interval = 3600000
    elif step == "minute":
        interval = 300000
    else:
        raise ValueError

    data = {}
    db = MysqlDB(host=BOSS_MYSQL_HOST)
    # step为"day"与step为"hour"或"minute"时, 查询的表不同, 表结构也有不同
    for timestamp in range(start_time, end_time, interval):
        sql_download = "select ifnull(sum(app), 0), ifnull(sum(cdn), 0), ifnull(sum(p2p), 0) "
        if step == "day":
            sql_download += "from boss_daily_download where customer_id = '{0}' and report_date = '{1}' "
            if domain is not None:
                sql_download += "and DNS = '{0}'".format(domain)
            date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
            app, cdn, p2p = db.execute(sql_download.format(customer_id, date)).one_by_one()
        else:
            sql_download += "from download_log_{0} where timestamp >= {1} and timestamp < {2} "
            if domain is not None:
                sql_download += "and DNS = '{0}'".format(domain)
            app, cdn, p2p = db.execute(sql_download.format(customer_id, timestamp, timestamp + interval)).one_by_one()
        app = round(app*8/(interval/1000), 2)
        cdn = round(cdn*8/(interval/1000), 2)
        p2p = round(p2p*8/(interval/1000), 2)
        sum = round((cdn + p2p)*8/(interval/1000), 2)
        data[str(timestamp)] = {"app": app, "cdn": cdn, "p2p": p2p, "sum": sum}
    del db

    return data


@print_trace
def down_minute_traffic_data(customer_id, start_time, domain_list=None):
    """
    下游客户 down_minute_traffic接口应该返回的data, data结构如下
    "data": {*domain: {"time": 1489507200000, "app_total_ratio": app/(cdn+p2p), "app": 0, "cdn": 0, "p2p": 0}}
    """
    if domain_list is None:
        pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
        domains = pg_db.execute("select domain_name from crm_customer_domain as d inner join crm_customer_info as i \
on d.customer = i.id where i.number = '{0}'".format(customer_id)).one_by_one()
        del pg_db
    else:
        domains = domain_list

    mysql_db = MysqlDB(host=BOSS_MYSQL_HOST)
    data = {}
    for dns in domains:
        app, cdn, p2p = mysql_db.execute("select ifnull(sum(app), 0) as app, ifnull(sum(cdn), 0) as cdn, ifnull(sum(p2p), 0) as p2p \
from download_log_{0} where timestamp >= {1} and timestamp < {2} and DNS = '{3}'"
                                   .format(customer_id, start_time, start_time + 300000, dns)).one_by_one()
        if (cdn + p2p) != 0:
            app_total_ratio = round(app / (cdn + p2p), 4)
        else:
            app_total_ratio = 0.0
        data[dns] = {"time": start_time, "app_total_ratio": app_total_ratio, "app": int(app), "cdn": int(cdn), "p2p": int(p2p)}
    del mysql_db

    return data


@print_trace
def customer_domain_read_data(customer_id, domain_list=None):
    """
    下游客户 customer_domain_read接口应该返回的data, data结构如下
    "data": [{"domain": domain1}, {"domain": domain2}, ...]
    """
    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)

    customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
    sql = "select domain_name as domain from crm_customer_domain where customer = {0} ".format(customer_index)

    if domain_list is None or len(domain_list) == 0:
        pass
    elif len(domain_list) == 1:
        sql += " and domain_name = '{0}'".format(domain_list[0])
    else:
        sql += " and domain_name in {0}".format(tuple(domain_list))

    data = pg_db.execute(sql).to_dict()
    del pg_db

    for domain in data:
        domain["domain"] = str(domain["domain"]).decode("utf-8")

    return data


# 上游客户接口
@print_trace
def up_traffic_info_data(customer_id, start_time, end_time, step):
    """
    上游客户 up_traffic_info接口应该返回的data, data结构如下
    "data": {*start_time: {"upload": 0}}
    """
    # 分api_block
    if step == "day":
        interval = 86400000
    elif step == "hour":
        interval = 3600000
    elif step == "minute":
        interval = 300000
    else:
        raise ValueError

    data = {}
    db = MysqlDB(host=BOSS_MYSQL_HOST)
    # step为"day"与step为"hour"或"minute"时, 查询的表不同, 表结构也有不同
    for timestamp in range(start_time, end_time, interval):
        sql_upload = "select ifnull(sum(upload), 0) "
        if step == "day":
            sql_upload += "from boss_daily_upload where customer_id = '{0}' and  report_date = '{1}'"
            date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
            upload = db.execute(sql_upload.format(customer_id, date)).only_one()
        else:
            sql_upload += "from upload_log_{0} where timestamp >= {1} and timestamp < {2}"
            upload = db.execute(sql_upload.format(customer_id, timestamp, timestamp + interval)).only_one()
        data[str(timestamp)] = {"upload": int(upload)}
    del db

    return data


@print_trace
def up_bandwidth_info_data(customer_id, start_time, end_time, step):
    """
    上游客户 up_bandwidth_info接口应该返回的data, data结构如下
    "data": {*start_time: {"upload": 0}}
    """
    # 分api_block
    if step == "day":
        interval = 86400000
    elif step == "hour":
        interval = 3600000
    elif step == "minute":
        interval = 300000
    else:
        raise ValueError

    data = {}
    db = MysqlDB(host=BOSS_MYSQL_HOST)
    # step为"day"与step为"hour"或"minute"时, 查询的表不同, 表结构也有不同
    for timestamp in range(start_time, end_time, interval):
        sql_upload = "select ifnull(sum(upload), 0) "
        if step == "day":
            sql_upload += "from boss_daily_upload where customer_id = '{0}' and  report_date = '{1}'"
            date = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
            upload = db.execute(sql_upload.format(customer_id, date)).only_one()
        else:
            sql_upload += "from upload_log_{0} where timestamp >= {1} and timestamp < {2}"
            upload = db.execute(sql_upload.format(customer_id, timestamp, timestamp + interval)).only_one()
        upload = round(upload*8/(interval/1000), 2)
        data[str(timestamp)] = {"upload": upload}
    del db

    return data


@print_trace
def up_activity_info_data(customer_id, start_day, end_day):
    """
    上游客户 activity_info接口应该返回的data, data结构如下
    "data": {*date: 0}
    """
    date_list = get_date_list_by_date(start_day, end_day)
    sql = "select ifnull(sum(daily), 0) from boss_daily_activities where custom_id = '{0}'and bill_date = '{1}'"

    db = MysqlDB(host=BOSS_MYSQL_HOST)
    data = {}
    for date in date_list:
        active = db.execute(sql.format(customer_id, date)).only_one()
        data[str(date)] = int(active)
    del db

    return data


if __name__ == "__main__":
    pass

    # sign = internal_api_sign(ACCESS_KEY_INTERNAL, SECRET_KEY_INTERNAL, TIMESTAMP_NOW)

    # 客户信息
    # result = {"msg": "",
    #           "timestamp": 1487040618,
    #           "data": {"100000001": {
    #               "prefixes": ["00000001", "00000002"],
    #               "table_info": {"upload_log": "upload_log_100000001",
    #                              "download_log": "download_log_100000001"},
    #               "blockinfo": {
    #                   "00000001": {
    #                       "download": {
    #                           "current": {
    #                               "category": "download",
    #                               "customer": "\u4e91\u7aef",
    #                               "prefix": "00000001",
    #                               "start_time": "00:00",
    #                               "interval": 240,
    #                               "to_bill": false},
    #                           "ts_into_effect": 1486396800,
    #                           "previous": {
    #                               "category": "download",
    #                               "customer": "\u4e91\u7aef",
    #                               "start_time": "00:00",
    #                               "interval": 300,
    #                               "prefix": "00000001",
    #                               "to_bill": false}},
    #                       "upload": {
    #                           "current": {
    #                               "category": "upload",
    #                               "customer": "\u4e91\u7aef",
    #                               "prefix": "00000001",
    #                               "start_time": "00:00",
    #                               "interval": 60,
    #                               "to_bill": true},
    #                           "ts_into_effect": 1486396800,
    #                           "previous": {
    #                               "category": "upload",
    #                               "customer": "\u4e91\u7aef",
    #                               "start_time": "00:00",
    #                               "interval": 300,
    #                               "prefix": "00000001",
    #                               "to_bill": true}}},
    #                   "00000002": {
    #                       "download": {
    #                           "current": {
    #                               "category": "download",
    #                               "customer": "\u4e91\u7aef",
    #                               "prefix": "00000002",
    #                               "start_time": "00:00",
    #                               "interval": 600,
    #                               "to_bill": true},
    #                           "ts_into_effect": 1486396800,
    #                           "previous": {
    #                               "category": "download",
    #                               "customer": "\u4e91\u7aef",
    #                               "start_time": "00:00",
    #                               "interval": 300,
    #                               "prefix": "00000002",
    #                               "to_bill": true}},
    #                       "upload": {
    #                           "current": {
    #                               "category": "upload",
    #                               "customer": "\u4e91\u7aef",
    #                               "prefix": "00000002",
    #                               "start_time": "00:00",
    #                               "interval": 120,
    #                               "to_bill": false},
    #                           "ts_into_effect": 1486396800,
    #                           "previous": {
    #                               "category": "upload",
    #                               "customer": "\u4e91\u7aef",
    #                               "start_time": "00:00",
    #                               "interval": 300,
    #                               "prefix": "00000002",
    #                               "to_bill": false}}}},
    #               "customer_id": "100000001"}},
    #           "success": true}

    # 计费规则信息
    # result = {"msg": "",
    #           "timestamp": 1487211125,
    #           "data": {"category": "flow",
    #                    "amount_unit": "GB",
    #                    "billing_strategy": "\u57fa\u7840\u8ba1\u8d39",
    #                    "params": "{\"price\": 0.95}",
    #                    "monetary_unit": "CNY"},
    #           "success": true}



