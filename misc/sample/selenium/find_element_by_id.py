# coding=utf-8
"""
selenium sample code

__author__ = 'zengyuetian'

"""

from selenium import webdriver
import time

if __name__ == "__main__":

    #profile = webdriver.FirefoxProfile(r'C:\Users\yunshang001\AppData\Roaming\Mozilla\Firefox\Profiles\9qttectw.default')
    #driver = webdriver.Firefox(profile)

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    time.sleep(2)

    driver.find_element_by_id("kw").send_keys("Selenium2")
    time.sleep(2)
    driver.find_element_by_id("su").click()

    driver.quit()

