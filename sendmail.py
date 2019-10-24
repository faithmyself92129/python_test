#!/usr/bin/python3

import smtplib 
from email.mime.text import MIMEText
from email.header import Header

sender = "from@runoob.com"
receivers = ["392617631@qq.com"]


mail_msg = """<p>Python youjianfasong...</p>
           <p><a href ="http://www.runoob.com"> lianjie </a></p>
           """  

message = MIMEText(mail_msg, "html","utf-8")
#message = MIMEText("Python sendmail ....", "plain",'utf-8')
message['From'] = Header('cainiaojiaocheng', 'utf-8')
message['To'] = Header("ceshi", 'utf-8')

subject = "Python SMTP ceshi "
message['Subject'] = Header(subject,'utf-8')

try:
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.sendmail(sender, receivers, message.as_string())
  print('SMTP send sucessful')
except smtplib.SMTPException:
  print("Error:send fail")






