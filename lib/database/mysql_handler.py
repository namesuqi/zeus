# coding=utf-8
"""
modified by dh 2016.08.04
"""
import binascii

from lib.database.mysqldb import MysqlDB
from lib.constant.database import *
from lib.decorator.trace import print_trace
from lib.utility.path import *

__author__ = 'zengyuetian'
'''
操作Mysql的上层库
'''


def db_restore_tb_box():
    """
    运行mysql命令，通过sql文件回滚数据库tbbox的内容
    :return: void
    """

    # sql文件路径
    sql_file = PathController.get_root_path() + "/misc/sql/tbbox.sql"

    login_str = "mysql -h{0} -u{1} -p{2}".format(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD)
    use_str = "use tbbox;"
    source_str = "source {0};".format(sql_file)

    command = '{0} -e "{1} {2} " '.format(login_str, use_str, source_str)
    print command
    os.system(command)


#########################################################################################
# User operation
#########################################################################################

def db_delete_user(username):
    """
    将指定用户的数据从mysql数据库中删除
    :param username:用户名
    :return:void
    """
    MysqlDB().delete("ppc_users", username=str(username))


def db_get_userid_by_name(username):
    """
    搜索用户相关信息
    :param username:用户名
    :return:
    """
    ids = MysqlDB().select("ppc_users", "id", username=str(username))
    user_id = ids[0][0]   # row 1 column 1
    return user_id


def db_create_prefix(prefix, uid=""):
    """
    往ppc_tenant_url_prefix中插入数据
    :param prefix:
    :param uid:用户id
    :return:
    """
    if (uid is not None) and (uid != ""):
        MysqlDB().insert("ppc_tenant_url_prefix", url_prefix=str(prefix), tenant_id=int(uid))
    else:
        MysqlDB().insert("ppc_tenant_url_prefix", url_prefix=str(prefix))


def db_delete_prefix(prefix):
    """
    将指定用户的数据从mysql数据库中删除
    :param prefix:
    :return:void
    """
    MysqlDB().delete("ppc_tenant_url_prefix", url_prefix=str(prefix))


def db_create_folder(tenant_id, dir_path):
    """
    往ppc_tenant_directory中插入数据
    :param tenant_id:用户id
    :param dir_path:目录路径
    :return:
    """
    MysqlDB().insert("ppc_tenant_directory", tenant_id=int(tenant_id), dir_path=str(dir_path))


def db_delete_folder(tenant_id, dir_path):
    """
    将指定用户的数据从mysql数据库中删除
    :param tenant_id:用户id
    :param dir_path:目录路径
    :return:
    """
    MysqlDB().delete("ppc_tenant_directory", tenant_id=int(tenant_id), dir_path=str(dir_path))


def db_add_user_file(sid, relative_url, file_id, active_prefix_id, source):
    """
    往ppc_tenant_files中插入数据
    :param sid:
    :param relative_url:
    :param file_id:
    :param active_prefix_id:
    :param source: source_url
    :return:
    """
    MysqlDB().insert("ppc_tenant_files", sid=int(sid), relative_url=str(relative_url), file_id=str(file_id),
                     active_prefix_id=str(active_prefix_id), source=str(source))


def db_delete_user_file(sid, relative_url):
    """
    在ppc_tenant_files里删除指定的文件
    :param sid:
    :param relative_url:
    :return:
    """
    MysqlDB().delete("ppc_tenant_files", sid=int(sid), relative_url=str(relative_url))


def db_add_blacklist(sid, relative_url, active_prefix_id):
    """
    往ppc_files_blacklist中插入数据
    :param sid:
    :param relative_url:
    :param active_prefix_id:
    :return:
    """
    MysqlDB().insert("ppc_files_blacklist", sid=int(sid), relative_url=str(relative_url),
                     active_prefix_id=str(active_prefix_id))


def db_delete_blacklist(sid, relative_url):
    """
    在ppc_files_blacklist里删除指定的文件
    :param sid:
    :param relative_url:
    :return:
    """
    MysqlDB().delete("ppc_files_blacklist", sid=int(sid), relative_url=str(relative_url))


def db_is_folder_exists(tenant_id, dir_path):
    """
    验证指定目录是否存在
    :param tenant_id: 用户id
    :param dir_path: 目录
    :return: 响应
    """
    results = MysqlDB().select("ppc_tenant_directory", "*", tenant_id=int(tenant_id), dir_path=str(dir_path))

    if len(results) > 0:
        return True
    else:
        return False


def db_is_prefix_exists(prefix):
    """
    验证指定prefix是否存在
    :param prefix:
    :return:
    """
    results = MysqlDB().select("ppc_tenant_url_prefix", "*", url_prefix=str(prefix))

    if len(results) > 0:
        return True
    else:
        return False


def db_get_info_by_fid(fid):
    """
    通过file_id获取文件信息
    :param fid:file_id
    :return:
    """
    file_id = binascii.a2b_hex(fid.lower())

    file_info = MysqlDB().select("ppc_tenant_files", "*", file_id=str(file_id))

    if len(file_info) != 0:
        size = file_info[0][5]
        md5 = binascii.b2a_hex(file_info[0][4])
        # binascii.b2a_hex(data)：将二进制数据字符串转换为十六进制编码
        source_url = file_info[0][13]
        active_prefix_id = file_info[0][12]
        prefix_list = MysqlDB().select("ppc_tenant_url_prefix", "url_prefix", id=active_prefix_id)
        # ppc_tenant_files中的active_prefix_id与ppc_url_prefix中的id相对应
        file_url = "http://" + prefix_list[0][0] + file_info[0][2]
        sourcetype_list = MysqlDB().select("ppc_tenant_source", "source_type", id=file_info[0][1])
        # sid=file_info[0][1], ppc_tenant_files中的sid与ppc_user_source中的id相对应
        source_type = sourcetype_list[0][0]
        ext = file_info[0][14]  # ?
        relative_url = file_info[0][2]

        return size, md5, source_url, file_url, source_type, ext, relative_url
    else:
        return file_info


def db_get_info_by_url(prefix, relative_url):
    """
    通过url的prefix和relative_url获取文件信息
    :param prefix:
    :param relative_url:
    :return:
    """
    prefix_info = MysqlDB().select("ppc_tenant_url_prefix", "*", url_prefix=str(prefix))
    file_info = MysqlDB().select("ppc_tenant_files", "*", active_prefix_id=prefix_info[0][0],
                                 relative_url=str(relative_url))
    file_id = binascii.b2a_hex(file_info[0][3]).upper()
    size = file_info[0][5]
    md5 = binascii.b2a_hex(file_info[0][4])
    file_url = prefix_info[0][2] + file_info[0][2]
    # file_url由ppc_url_prefix中的prefix和ppc_user_files中的relative_url组成
    return file_id, size, md5, file_url


def db_get_info_by_md5(md5):
    """
    通过文件的MD5获取文件信息
    :param md5:
    :return:
    """
    md5 = binascii.a2b_hex(md5.upper())
    file_info = MysqlDB().select("ppc_tenant_files", "*", md5=str(md5))

    if len(file_info) == 0:  # 判断数据库是否有指定数据，如果无数据，返回False
        return file_info
    else:
        file_id = binascii.b2a_hex(file_info[0][3]).upper()
        size = file_info[0][5]
        is_public = str(file_info[0][10])
        relative_url = str(file_info[0][2])
        active_prefix_id = file_info[0][12]
        prefix_list = MysqlDB().select("ppc_tenant_url_prefix", "url_prefix", id=active_prefix_id)
        # ppc_tenant_files中的active_prefix_id与ppc_tenant_url_prefix中的id相对应
        file_url = prefix_list[0][0] + relative_url
        return file_id, size, is_public, relative_url, file_url


def db_get_file_count_by_uid(uid, source_type=None):
    """
    通过用户id获取用户OSS以外的其他源数据数目
    :param uid:用户id
    :param source_type:可选参数，默认获取所有源数据，可单独指定一种 OSS / M3U8
    :return:
    """
    if source_type in (None, ""):
        cdn_id = MysqlDB().select("ppc_tenant_source", "id", tenant_id=int(uid), source_type='CDN')
        cdn_files = MysqlDB().select("ppc_tenant_files", "*", sid=cdn_id[0][0])
        m3u8_id = MysqlDB().select("ppc_tenant_source", "id", tenant_id=int(uid), source_type='M3U8')
        m3u8_files = MysqlDB().select("ppc_tenant_files", "*", sid=m3u8_id[0][0])
        # ppc_tenant_source中的sourceType与ppc_tenant_files中的sid相对应
        filecount = len(cdn_files) + len(m3u8_files)
    else:
        ids = MysqlDB().select("ppc_tenant_source", "id", tenant_id=int(uid), source_type=str(source_type))
        if len(ids) == 0:
            filecount = 0
        else:
            files = MysqlDB().select("ppc_tenant_files", "*", sid=ids[0][0])
            filecount = len(files)

    return filecount


def db_delete_file_by_md5(md5):
    """
    根据文件的MD5信息，在ppc_tenant_files中删除指定文件
    :param md5:
    :return:
    """
    md5 = binascii.a2b_hex(md5.upper())
    MysqlDB().delete("ppc_tenant_files", md5=str(md5))


def db_delete_file_by_url(url):
    """
    根据文件的url信息，在ppc_tenant_files中删除指定文件
    :param url:source_url
    :return:
    """
    MysqlDB().delete("ppc_tenant_files", source=str(url))


def db_delete_flv_by_url(url):
    """
    根据文件的url信息，在ppc_tenant_live_channel中删除指定文件
    :param url:source_url
    :return:
    """
    MysqlDB().delete("ppc_tenant_live_channel", output_url=str(url))


def db_get_info_by_output_url(source):
    """
    通过文件的output_url获取文件信息
    :param source:output_url
    :return:
    """
    if source.startswith('http://'):
        source_url = source
    else:
        source_url = "http://" + source

    file_info = MysqlDB().select("ppc_tenant_live_channel", "*", output_url=str(source_url))

    if len(file_info) != 0:
        file_id = file_info[0][2]
        file_url = file_info[0][3]
        return file_id, file_url
    else:
        return file_info


def db_check_file_exist(user_id, file_path, source_type=None):
    """
    检测指定用户的指定文件是否存在
    :param user_id:用户id
    :param file_path:文件路径
    :param source_type:用户的数据源类型
    :return:响应
    """
    if source_type in (None, ""):
        source_type = "OSS"

    ids = MysqlDB().select("ppc_tenant_source", "id", tenant_id=int(user_id), source_type=str(source_type))
    sid = ids[0][0]  # ppc_user_files中的sid与ppc_user_source中的id相对应
    results = MysqlDB().select("ppc_tenant_files", "*", sid=int(sid), relative_url=str(file_path))

    if len(results) > 0:
        return True
    else:
        return False


def db_get_info_by_source_url(source):
    """
    通过文件的source_url获取文件信息
    :param source:source_url
    :return:
    """
    if source.startswith('http://'):
        source_url = source
    else:
        source_url = "http://" + source

    file_info = MysqlDB().select("ppc_tenant_files", "*", source=str(source_url))

    if len(file_info) != 0:
        file_id = binascii.b2a_hex(file_info[0][3]).upper()
        file_size = file_info[0][5]
        active_prefix_id = file_info[0][12]
        prefix_list = MysqlDB().select("ppc_tenant_url_prefix", "url_prefix", id=active_prefix_id)
        # ppc_tenant_files中的id与ppc_tenant_url_prefix中的active_prefix_id相对应
        file_url = "http://" + prefix_list[0][0] + file_info[0][2]
        sourcetype_list = MysqlDB().select("ppc_tenant_source", "source_type", id=file_info[0][1])
        # sid=file_info[0][1], ppc_tenant_files中的sid与ppc_tenant_source中的id相对应
        source_type = sourcetype_list[0][0]
        file_source = file_info[0][13]
        psize = file_info[0][6]
        ppc = file_info[0][7]

        return file_id, file_size, file_url, source_type, file_source, psize, ppc
    else:
        return file_info


def db_add_user_no_prefix(username, password):

    mysql_handle = MysqlDB()
    mysql_handle.insert('ppc_tenants', name=username, license_verify=0)
    ids = mysql_handle.select('ppc_tenants', 'id', name=username)
    if len(ids) != 0:
        account_id = int(ids[0][0])
        password = 'salt'+password
        import hashlib
        m = hashlib.md5()
        m.update(password)
        password = m.hexdigest()
        import time
        time_string = time.strftime('%Y-%m-%d %H:%M:%S')

        mysql_handle.insert('ppc_users', id=account_id, tenant_id=account_id, username=username,
                         password=password, salt='salt', phone='11133333333', email='tester@cloutropy.com',
                         verify_code='verify_code', create_time=time_string
                         )
        mysql_handle.insert('ppc_user_group', user_id=account_id, group_id='3')
    else:
        print "#############################################"
        print "###        create account fail            ###"
        print "#############################################"


def db_delete_user_no_prefix(username):

    mysql_handle = MysqlDB()
    ids = mysql_handle.select('ppc_tenants', 'id', name=username)
    if len(ids) != 0:
        account_id = int(ids[0][0])
        mysql_handle.delete('ppc_user_group', user_id=account_id)
        mysql_handle.delete('ppc_users', username=username)
        mysql_handle.delete('ppc_tenants', name=username)
    else:
        print "#############################################"
        print "###   no such account, pls check out!     ###"
        print "#############################################"

    #########################################################################################
    # File operation
    #########################################################################################


@print_trace
def db_get_ops_host_by_host_id(host_id):
    """
    从ops_host表中获取host_id对应的数据
    :param host_id:
    :return:
    """
    ids = MysqlDB(database=MYSQL_CONTROL).select("ops_host", "*", host_id=str(host_id))
    return ids


@print_trace
def db_get_ops_host_info_by_host_id(host_id):
    """
    从ops_host_info表中获取host_id对应的数据
    :param host_id:
    :return:
    """
    ids = MysqlDB(database=MYSQL_CONTROL).select("ops_host_info", "*", host_id=str(host_id))
    return ids


@print_trace
def db_insert_ops_host(host_id, ip, status):
    """
    在ops_host中插入一条记录
    :param host_id:
    :param ip:
    :param status:
    :return:
    """
    MysqlDB(database=MYSQL_CONTROL).insert('ops_host', host_id=host_id, ip=ip, status=status)


@print_trace
def db_update_ops_host(update_key, update_value, host_id=None):
    """
    将某个数据库中所有数据的某个字段的值更新,若传入参数host_id，则只更新host_id对应的数据
    :param update_key:
    :param update_value:
    :param host_id:
    :return:
    """
    if host_id is None:
        MysqlDB(database=MYSQL_CONTROL).update('ops_host', update_key, update_value)
    else:
        MysqlDB(database=MYSQL_CONTROL).update('ops_host', update_key, update_value, host_id=host_id)


@print_trace
def db_update_ops_host_info(update_key, update_value, host_id=None):
    """

    :param update_key:
    :param update_value:
    :param host_id:
    :return:
    """
    if host_id is None:
        MysqlDB(database=MYSQL_CONTROL).update('ops_host_info', update_key, update_value)
    else:
        MysqlDB(database=MYSQL_CONTROL).update('ops_host_info', update_key, update_value, host_id=host_id)


@print_trace
def db_insert_ops_host_info(host_id, hostname, comment, location, cpu_count, mem_capacity, disk_capacity, os):
    """
    在ops_host_info中插入一条记录
    :param host_id:
    :param hostname:
    :param comment:
    :param location:
    :param cpu_count:
    :param mem_capacity:
    :param disk_capacity:
    :param os:
    :return:
    """
    # print host_id, ip, status
    MysqlDB(database=MYSQL_CONTROL).insert('ops_host_info', host_id=host_id, hostname=hostname, comment=comment,
                                           location=location, cpu_count=cpu_count, mem_capacity=mem_capacity,
                                           disk_capacity=disk_capacity, os=os)


@print_trace
def db_delete_ops_host_info(host_id=None):
    """
    通过host_id在ops_host_info中删除对应记录,若无host_id传入，将清空整张表，清表请慎重
    :param host_id:
    :return:
    """
    if host_id is None:
        MysqlDB(database=MYSQL_CONTROL).delete('ops_host_info')
    else:
        MysqlDB(database=MYSQL_CONTROL).delete('ops_host_info', host_id=host_id)


@print_trace
def db_delete_ops_host(host_id=None):
    """
    通过host_id在ops_host中删除对应记录,若无host_id传入，将清空整张表，清表请慎重
    :param host_id:
    :return:
    """
    if host_id is None:
        MysqlDB(database=MYSQL_CONTROL).delete('ops_host')
    else:
        MysqlDB(database=MYSQL_CONTROL).delete('ops_host', host_id=host_id)


@print_trace
def db_delete_host_current_server(host_id):
    """
    通过host_id在ops_host_info中删除对应记录
    :param host_id:
    :return:
    """
    MysqlDB(database=MYSQL_CONTROL).delete('ops_host_current_server', host_id=host_id)


def db_insert_host_current_server(server_role_id, host_id):
    """
    在ops_host_current_server中插入一条记录
    :param server_role_id:
    :param host_id:
    :return:
    """
    MysqlDB(database=MYSQL_CONTROL).insert('ops_host_current_server', server_role_id=server_role_id, host_id=host_id)


######################################
# for unit testing
######################################
# if __name__ == "__main__":
    # MysqlHandler().RestoreTbbox()
    # sourcetype = None
    # if sourcetype in (None, "True", "true"):
    #     print True
    # db_delete_user_no_prefix('tester')
    # db_add_user_no_prefix('tester', '123456')
    # print db_get_ops_host_by_host_id("2c964006b984468ea2a2eab24c7d14cf")
