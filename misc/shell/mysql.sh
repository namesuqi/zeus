#!/usr/bin/env bash

# author: Zeng YueTian
# date: 2016/01/05


MYSQL_HOST="10.5.100.21"
MYSQL_USER="ppc"
MYSQL_PASS="yunshang2014"


# prepare mysql data
function restore_mysql()
{
    echo ---------------------------------------------------------------------------
    echo Start to restore mysql database of $MYSQL_HOST with $MYSQL_USER
    mysql -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PASS -e "use tbbox; source ./misc/sql/tbbox.sql;"
    echo ---------------------------------------------------------------------------
}




