#coding:utf-8
from page.page_locator import location_lootor
class do_next_job:
    def __init__(self,driver):
        self.do_something = location_lootor(driver)
    #点击跳转至登录页面
    def click_to_loging(self):
        self.do_something.email_button().click()
    #输入密码值
    def send_meg(self):
        self.do_something.get_code_passwd().send_keys("dsrfuck1qie")
    #点击确定跳转至首页
    def click_button(self):
        self.do_something.get_login_button().click()

