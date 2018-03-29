# coding=utf-8
"""

boss系统 环境相关的常量

__author__ = 'liwenxuan'

"""

# # 本地自动化环境用
BOSS_ENVIRONMENT = "sh_office_auto"

# # 本地测试环境用
# BOSS_ENVIRONMENT = "sh_office_test"


if BOSS_ENVIRONMENT == "sh_office_auto":

    # CRM
    BOSS_CRM_HOST = "192.168.4.200"
    BOSS_CRM_PORT = 8069

    # PostgreSQL   Boss-CRM
    BOSS_POSTGRESQL_DATABASE = "boss_crm"
    BOSS_POSTGRESQL_USER = "odoo"
    BOSS_POSTGRESQL_PASSWORD = "odoo"
    BOSS_POSTGRESQL_HOST = "192.168.4.200"
    BOSS_POSTGRESQL_PORT = 5432

    # MySQL   Boss-Bill/Panel
    BOSS_MYSQL_DATABASE = "boss_bills"
    BOSS_MYSQL_USER = "boss"
    BOSS_MYSQL_PASSWORD = "boss"
    BOSS_MYSQL_HOST = "192.168.4.200"
    BOSS_MYSQL_PORT = 3306

    # kafka
    KAFKA_HOSTS = "192.168.4.230:9092,192.168.4.231:9092,192.168.4.232:9092"
    SCHEMA_HOST = "192.168.4.230"
    SCHEMA_PORT = 8081
    CONSUMER_GROUP = "boss_bill_daily_test"

elif BOSS_ENVIRONMENT == "sh_office_test":

    # CRM
    BOSS_CRM_HOST = "192.168.1.170"
    BOSS_CRM_PORT = 8069

    # PostgreSQL   CRM
    BOSS_POSTGRESQL_DATABASE = "boss_crm"
    BOSS_POSTGRESQL_USER = "odoo"
    BOSS_POSTGRESQL_PASSWORD = "odoo"
    BOSS_POSTGRESQL_HOST = "192.168.1.170"
    BOSS_POSTGRESQL_PORT = 5432

    # MySQL   Bill/Panel
    BOSS_MYSQL_DATABASE = "boss_bills"
    BOSS_MYSQL_USER = "boss"
    BOSS_MYSQL_PASSWORD = "boss"
    BOSS_MYSQL_HOST = "192.168.1.170"
    BOSS_MYSQL_PORT = 3306

    # kafka
    KAFKA_HOSTS = "192.168.1.230:9092,192.168.1.232:9092,192.168.1.191:9092,192.168.1.189:9092"
    SCHEMA_HOST = "192.168.1.230"
    SCHEMA_PORT = 8081
    CONSUMER_GROUP = "boss_bill_test"

else:
    print "environment param error!"
    raise ValueError
