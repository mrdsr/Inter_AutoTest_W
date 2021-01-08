#coding:utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText


class sendEmil:
    def send_to_message(self):
        mail_host = 'smtp.163.com'
        mail_user = 'mrdaishuangrong@163.com'
        mail_pwd = 'dai19940812'

        sender = 'mrdaishuangrong@163.com'
        receivers = 'daishuangrong@dhibank.com'

        content = 'hello wrold'

        message = MIMEText(content,'plain','utf-8')
        message['From'] = "{}".format(sender)
        message['To'] = "我是你爸爸我真伟大"
        message['Title'] = '这是TestCase'
        subject = 'Python~~~~~~~~~Test'
        message['Subject'] = Header(subject, 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(mail_user, mail_pwd)
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        print("发送成功")


a = sendEmil()
a.send_to_message()