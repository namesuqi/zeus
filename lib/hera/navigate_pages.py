# coding=utf-8
# author: zengyuetian
# 用来展示jenkins, hera各个页面
# 下载chromedriver.exe，复制到Python安装目录的Scripts目录，将该目录加到PATH环境变量中。

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

NAVIGATE_URLS = [
    # "http://10.3.0.16:5000/feature_test_progress",
    # "http://10.3.0.16:5000/regression_progress",
    # "http://10.3.0.16:5000/bug_info",
    # "http://10.3.0.16:5000/bug_status",
    # "http://10.3.0.16:5000/unit_test",
    # "http://10.3.0.16:5000/auto_test",
    # "http://10.3.0.16:5000/manual_test",
    # "http://10.3.0.16:5000/auto_rate",
    # "http://10.3.0.16:5000/jenkins_builds",
    # "http://10.4.0.1:8080/view/Deploy-Build/",
    # "http://10.4.0.1:8080/view/Server-Test/",
    # "http://10.4.0.1:8080/view/SDK-Test/",
    "http://jenkins.crazycdn.cn/view/Local_Vod_Test/",
    "http://jenkins.crazycdn.cn/view/VOD-Auto/"
]

TIME_OUT = 1
TIME_PAGE_STAY = 30

# jenkins_user = "tester"
# jenkins_passwd = "OrrtOmDn2RwV"

jenkins_user = "zengyuetian"
jenkins_passwd = "vliQh3U2byob"

# 消除 --ignore-certificate-error 的chrome警告
option = webdriver.ChromeOptions()
option.add_argument("test-type")
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", chrome_options=option)
driver.implicitly_wait(TIME_OUT)


driver.maximize_window()
time.sleep(2)

# 登录jenkins先
driver.get("http://jenkins.crazycdn.cn//login?from=%2F")
driver.find_element(By.XPATH, '//*[@id="j_username"]').send_keys(jenkins_user)
driver.find_element(By.XPATH, '//*[@id="main-panel"]/div/form/table/tbody/tr[2]/td[2]/input').send_keys(jenkins_passwd)
driver.find_element(By.XPATH, '//*[@id="yui-gen1-button"]').click()

# 页面轮展
while True:
    for url in NAVIGATE_URLS:
        time.sleep(TIME_PAGE_STAY)
        driver.get(url)
