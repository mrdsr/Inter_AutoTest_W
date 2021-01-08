#coding:utf-8

from appium import webdriver

class runBefor:

    def get_driver(self):
      capabilities = {
        "platformName": "Android",
        # "automationName":"UiAutomator2",
        "deviceName": "emulator-5554",
        "app": "/Users/shuangrongdai/Downloads/imooc7.2.110102001android.apk",
        "appWaitActivity" : "com.imooc.component.imoocmain.index.MCMainActivity",
        'newCommandTimeout':4000,
        "noReset":"true"
      }

      driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
      return driver