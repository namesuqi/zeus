# coding=utf-8
__author__ = 'jinyifan'


class Verify(object):
    def VerifyLarger(self, actual, expect):
        if float(actual) <= float(expect):
            raise AssertionError("Actual {0}, expect {1}".format(actual, expect))

    def VerifySmaller(self, actual, expect):
        if float(actual) >= float(expect):
            raise AssertionError("Actual {0}, expect {1}".format(actual, expect))