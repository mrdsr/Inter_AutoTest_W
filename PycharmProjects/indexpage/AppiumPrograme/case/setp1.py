#coding:utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import time
from appium import webdriver
from case.runBefor import runBefor
from bussies.login import login_busses
from HtmlTestRunner import HTMLTestRunner
from report.send_yagmail import send_report

class runCase(unittest.TestCase):

    def setUp(self):
        print("Case要开始啦")
        self.driver = runBefor().get_driver()
    def test_01(self):
        self.case = login_busses(self.driver)
        self.case.login()
        print("----------------",end='')
        print("测试通过，case执行完成",end='')
        print("----------------")
    def test_02(self):
       pass
    def tearDown(self):
        self.driver.quit()
        print("Case结束了")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(runCase('test_01'))
    now = time.strftime("%Y-%m-%d", time.localtime())
    file_path = now + ".html"
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="appium测试计划",
        tester="超级计划代双荣"
    )
    runner.run(suite)
    fp.close()
    send_report = send_report()
    send_report.send_report_to()
    a = False