import smtplib
from email.header import Header

from email.mime.text import MIMEText


mail_smtp ='smtp.163.com'
mail_user = 'mrdaishuangrong@163.com'
mail_pwd = 'dai19940812'
#发送邮箱
sender = 'mrdaishuangrong@163.com'

#收件人
reverser = 'daishuangrong@dhibank.com'
#请求内容
neirong = '我是你爸爸我真伟大，养你这么大'
message = MIMEText(neirong,'plain','utf-8')
#邮件标题
biaoti  = "我是个大帅比"
message['Title'] = 'appiumTestCase'
message['Subject'] = Header(biaoti,'utf-8')

#从哪来到哪去

smtp = smtplib.SMTP()
smtp.connect(mail_smtp)
smtp.login(mail_user,mail_pwd)
smtp.sendmail(sender,reverser,message.as_string())
smtp.close()