# coding=utf-8

"""

测试过程或自动化用例使用的一些额外的函数

__author__ = 'liwenxuan'

"""

import hashlib
from lib.database.postgresql_db import PostgresqlDB
from lib.interface.boss.environment_constant import BOSS_POSTGRESQL_HOST


# 生成鉴权参数sign
def make_api_param_sign(api_access_key, api_secret_key, sign_timestamp, md5=True):
    """
    boss接口的鉴权参数sign
    :param api_access_key: 该信息从BOSS CRM获取
    :param api_secret_key: 该信息从BOSS CRM获取
    :param sign_timestamp: 应与接口参数timestamp值一致, 单位为秒, 非负整数
    :param md5: 是否进行MD5加密
    :return:
    """
    sign = str(api_access_key) + str(api_secret_key) + str(sign_timestamp)
    if md5 is True:
        sign = hashlib.md5(sign).hexdigest()
    return sign


# 生成请求参数domain_names
def make_api_param_domain_names(field, domain_list):
    """
    boss下游客户域名相关接口的请求参数domain_names
    :param field: 字段名, "domain_name"
    :param domain_list: N个domain组成的list
    :return:
    """
    assert isinstance(domain_list, list)
    domain_names = []
    for domain in domain_list:
        domain_name = {field: domain}
        domain_names.append(domain_name)
    return domain_names


def check_domains(customer_id, *domain_lists):
    # boss下游客户域名相关接口用, 确认指定客户的指定域名存在
    domain_list = []
    for one_domain_list in domain_lists:
        domain_list += one_domain_list

    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
    sql = "select domain_name from crm_customer_domain where customer = {0} ".format(customer_index)
    if len(domain_list) == 0:
        pass
    elif len(domain_list) == 1:
        sql += "and domain_name = '{0}'".format(domain_list[0])
    else:
        sql += "and domain_name in {0}".format(tuple(domain_list))
    print sql

    real_domain_list = pg_db.execute(sql).one_by_one()
    del pg_db

    if real_domain_list == domain_list:
        return True
    else:
        return False


def select_domains(customer_id, *domain_lists):
    # boss下游客户域名相关接口用, 查询指定客户的指定域名是否存在
    domain_list = []
    for one_domain_list in domain_lists:
        domain_list += one_domain_list

    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
    sql = "select domain_name from crm_customer_domain where customer = {0} ".format(customer_index)
    if len(domain_list) == 0:
        pass
    elif len(domain_list) == 1:
        sql += "and domain_name = '{0}'".format(domain_list[0])
    else:
        sql += "and domain_name in {0}".format(tuple(domain_list))
    print sql

    data = pg_db.execute(sql).one_by_one()
    del pg_db

    return data


def delete_domains(customer_id, domain_list):
    # boss下游客户域名相关接口用, 删除指定客户的指定域名, 可一次删除多个
    assert isinstance(domain_list, list)
    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
    sql = "delete from crm_customer_domain where customer = {0} and ".format(customer_index)
    if len(domain_list) == 0:
        raise ValueError
    elif len(domain_list) == 1:
        sql += "domain_name = '{0}'".format(domain_list[0])
    else:
        sql += "domain_name in {0}".format(tuple(domain_list))

    data = pg_db.execute(sql)
    del pg_db

    return data


def delete_domains_except(customer_id, domain_list):
    # boss下游客户域名相关接口用, 删除指定客户的指定域名以外的其他该客户的域名, 可一次删除多个
    assert isinstance(domain_list, list)
    pg_db = PostgresqlDB(host=BOSS_POSTGRESQL_HOST)
    customer_index = pg_db.execute("select id from crm_customer_info where number = '{0}'".format(customer_id)).only_one()
    sql = "delete from crm_customer_domain where customer = {0} and ".format(customer_index)
    if len(domain_list) == 0:
        raise ValueError
    elif len(domain_list) == 1:
        sql += "domain_name != '{0}'".format(domain_list[0])
    else:
        sql += "domain_name not in {0}".format(tuple(domain_list))

    data = pg_db.execute(sql)
    del pg_db

    return data


if __name__ == "__main__":
    pass
    # print make_api_param_domain_names("domain_name", "domain1", "domain2")

