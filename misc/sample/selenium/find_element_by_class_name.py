# coding=utf-8
"""
selenium sample code

__author__ = 'zengyuetian'

"""

from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    time.sleep(2)
    driver.find_element_by_class_name("s_ipt").send_keys("Selenium2")
    time.sleep(2)
    driver.find_element_by_class_name("s_btn").click()  # 使用多个class中的某个可以区分的class即可
    driver.quit()