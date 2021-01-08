import yagmail
# from case.setp1 import runCase
import time
class send_report:
    def __init__(self):
        self.now = time.strftime("%Y-%m-%d",time.localtime())
    def send_report_to(self):
        self.now_time_path = self.now+'.html'
        #开始发送邮件
        yag = yagmail.SMTP(user='mrdaishuangrong@163.com',password='dai19940812',host='smtp.163.com')
        file_path = '/Users/shuangrongdai/PycharmProjects/indexpage/AppiumPrograme/case/%s' %self.now_time_path
        connect = ['我是yagmail发送的',file_path]

        yag.send('daishuangrong@dhibank.com','newTest-appium',contents=connect)
