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
    driver.find_element_by_link_text("新闻").click()
