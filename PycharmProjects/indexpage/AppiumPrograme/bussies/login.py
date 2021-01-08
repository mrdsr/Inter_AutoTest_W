#coding:utf-8
import time

from handle.do_something import do_next_job

class login_busses:
    def __init__(self,driver):
        self.handle = do_next_job(driver)
    #登录业务

    def login(self):
        time.sleep(5)
        self.handle.click_to_loging()
        self.handle.send_meg()
        self.handle.click_button()

