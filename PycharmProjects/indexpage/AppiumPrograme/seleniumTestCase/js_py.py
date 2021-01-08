#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("我是你爸爸")

time.sleep(3)

driver.find_element_by_xpath('//*[@id="su"]').click()

#js代码

js = "var q = document.documentElement.scrollTop=100000"

driver.execute_script(js)
time.sleep(2)
