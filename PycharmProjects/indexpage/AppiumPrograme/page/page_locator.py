#coding:utf-8
from util.by_local_element import find_element
#登录
class location_lootor:
    def __init__(self,driver):
        # self.driver = driver
        self.get_loctor = find_element(driver)
    #获取账号
    def get_code_num(self):
        # self.get_loctor.chooies_element('getEmail')
        pass

    #获取密码
    def get_code_passwd(self):
        return self.get_loctor.chooies_element('pwd')
    #点击登录
    def get_login_button(self):
        return self.get_loctor.chooies_element('loginButton')
    #点击邮箱跳转登录页面的button
    def email_button(self):
        return self.get_loctor.chooies_element('getEmail')