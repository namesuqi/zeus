# coding=utf-8
# author: zengyuetian


from testlink import *
url = 'http://testlink.crazycdn.cn/lib/api/xmlrpc/v1/xmlrpc.php' #ip地址为安装的testlink ip
key = 'a06641a2cea5d780ae685beea32dcef0' # API key
tlc = TestlinkAPIClient(url, key)

# 获得所有的测试套件和它下面的测试用例数目
# projects = tlc.getProjects()
# animbus = projects[0] #因为只有一个测试项目，故为0
# topSuites = tlc.getFirstLevelTestSuitesForTestProject(animbus['id'])
# #len(topSuites)
# #6
# suite = topSuites[0]
# for suite in topSuites:
#     # print suite['id'], suite['name']
#     print suite
#     test_cases = tlc.getTestCasesForTestSuite(suite['id'], 10, "")
#     print len(test_cases)



# 下面这些是获得制定test plan的case和每个case的进度

tp = tlc.getTestPlanByName("Test Case", "SDK_3.9发布测试计划_RC3")

totals = tlc.getTotalsForTestPlan(2738)
print tp
print totals

tcs = tlc.getTestCasesForTestPlan(2738)
print tcs
print len(tcs)





