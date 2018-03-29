# System Testing Automation Framework
Author: Zeng YueTian  
Based on: robot framework + python  

 

## Purpose
Integrate server, sdk, live, platform, performance test into one test framework.  

## Documentation
misc/doc/*

## File Structure
    lib: Test Library, Test Keyword
    misc: kinds of related files
    result: test result folder for log and report
    testsuite: test suite, test cases
        apk: android sdk test
        feature: feature test
        platform: data platform
        sdk: yunshang client
        server: server API
        special: NAT and so on
        web: boss
    utility: test tools
    run.py: test entrance, see its file header for usage
    check_result.sh: jenkins integrated script to check if test pass
    
## Setup test environment
    apt-get update
    apt-get install python-setuptools
    apt-get install python-pip
    apt-get install mysql-client-core-5.5    
    apt-get install python-dev or yum install python-devel
    apt-get install libmysqld-dev or yum install mysql-devel
    apt-get install postgresql
    apt-get install libpq-dev

    then run pip install -r requirements.txt
    
    apt-get install apache2
    apt-get install curl
    apt-get install expect
    apt-get install sshpass or yum install sshpass
    pip install MySQL-python
    pip install dpkt
    pip install redis-py-cluster
    pip install pymongo
    pip install redis
    pip install robotframework -i http://pypi.v2ex.com/simple
    pip install MySQL-python -i http://pypi.v2ex.com/simple
    pip install robotframework-httplibrary -i http://pypi.v2ex.com/simple
    pip install pymongo -i http://pypi.v2ex.com/simple
    pip install redis -i http://pypi.v2ex.com/simple
    pip install robotremoteserver -i http://pypi.v2ex.com/simple
    download rediscluster and python setup.py install


## Create test lib or test case
    think about running on different test environment
    use cross-platform solution
    involve new library only if necessary
    follow the coding standard
