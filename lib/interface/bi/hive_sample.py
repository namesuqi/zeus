# coding=utf-8
"""

linux上安装pyhive的步骤:
    1. pip install pyhive
    2. pip install thrift
    3. pip install sasl
    4. pip install thrift_sasl
    5. yum install cyrus-sasl-plain  cyrus-sasl-devel  cyrus-sasl-gssapi

__author__ = 'liwenxuan'


"""

from pyhive import hive

HIVE_HOST = "192.168.3.197"
HIVE_PORT = 10000


# windows上无法运行
def hive_sample(command, file_name, hive_host=HIVE_HOST, hive_port=HIVE_PORT):
    hive_conn = hive.connect(hive_host, port=hive_port)
    cursor = hive_conn.cursor()
    # cursor.execute('set hive.cli.print.header=true')
    cursor.execute(command)
    results = cursor.fetchall()

    file = open(file_name, "w")
    for result in results:
        file.write(str(result))
    file.close()
    print "Create", file_name

    cursor.close()
    hive_conn.close()


if __name__ == "__main__":
    hive_sample("select * from dim_count_level_key", "dim_count_level_key.txt")
    hive_sample("select * from dim_customer_key", "dim_customer_key.txt")
    hive_sample("select * from dim_date_key", "dim_date_key.txt")
    hive_sample("select * from dim_duration_level_key", "dim_duration_level_key.txt")
    hive_sample("select * from dim_ip_key", "dim_ip_key.txt")
    hive_sample("select * from dim_nat_key", "dim_nat_key.txt")
    hive_sample("select * from dim_sdk_version_key", "dim_sdk_version_key.txt")
    # hive_sample("select * from dim_srv_key", "dim_srv_key.txt")
    hive_sample("select * from dim_time_key", "dim_time_key.txt")


