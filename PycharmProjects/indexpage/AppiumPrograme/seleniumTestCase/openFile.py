#coding:utf-8
import os

from selenium import webdriver

driver = webdriver.Chrome()
 #打开上传功能页面
file_path = 'file:///' + os.path.abspath('/Users/shuangrongdai/PycharmProjects/indexpage/AppiumPrograme/seleniumTestCase/case.html')
driver.get(file_path)
#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('/Users/shuangrongdai/Desktop/图片/WechatIMG315.png')