#!/bin/bash

# the main entrance for auto test

# author: Zeng YueTian
# date: 2016/01/04



######################################################
# If any fail, exit 1 to make jenkins build fail
######################################################
echo Check result start.
result=`grep FAIL result/output.xml`
echo $result
echo ${#result}  # result string length
if [ ${#result} -gt 0 ]; then
    echo SDK Auto Test Failed.
    exit 1
fi
echo Check result done.