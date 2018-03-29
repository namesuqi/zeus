# coding=utf-8
__author__ = 'Zeng YueTian'

"""
验证响应的核心库
modified by dh 2016.08.03
"""


def status_code_should_be_equal(response, expected_status_code):
    """
    验证返回的状态码
    :param response:响应体
    :param expected_status_code:期望状态码
    :return:void
    """
    try:
        print "Real status code:   ", response.status_code
        print "Expected status code: ", expected_status_code
        if str(response.status_code) != str(expected_status_code):
                raise AssertionError('http request response is: %s\n'
                                     'expected: %s'
                                     % (response.status_code, expected_status_code))
    except Exception as err:
        raise AssertionError('Verify status code fail:\n%s' % err)


def error_code_should_be_equal(response, expected_err_code=None):
    """
    验证返回的错误码
    :param response:响应体
    :param expected_err_code:期望错误码
    :return:void
    """
    try:
        real_err_code = response.json().get('error', None)
    except:
        real_err_code = None

    print "Real error code:    ", real_err_code
    print "Expect error code:  ", expected_err_code

    if str(real_err_code) != str(expected_err_code):
        raise AssertionError('http request response is: %s\nexpected: %s'
                             % (real_err_code, expected_err_code))


def error_code_should_cover(response, *args):
    """
    验证返回的错误码应该为可能出现的错误码中某一个
    :param response:响应体
    :return:void
    """
    try:
        real_err_code = response.json().get('error', None)
    except:
        real_err_code = None

    print "Real error code:    ", real_err_code
    print "Expect error code:  ", str(args)

    if str(real_err_code) not in (str(args)):
        raise AssertionError('http request response is: %s\nexpected: %s'
                             % (real_err_code, args))


def field_should_be_exist(response, field):
    """
    验证指定域存在
    :param response:响应体
    :param field:域
    :return:void
    """
    try:

        if response.json().has_key(field):
            exists = True
        else:
            exists = False
    except Exception as err:
        print err.message
        exists = False

    if not exists:
        raise AssertionError('Field %s not exist' % field)


def hget_field_value_should_not_be_exist(value):
    """
    验证hegt的值存在
    :param value:响应体
    :return:void
    """
    try:
        if value is not None:
            exists = True
        else:
            exists = False
    except Exception as err:
        print err.message
        exists = False

    if exists:
        raise AssertionError('hget response wrong!')


def verify_push_data(response_list):
    flag = False
    for response in response_list:
        if response[0:4] == 'b107':
            flag = True
            break
    return flag



