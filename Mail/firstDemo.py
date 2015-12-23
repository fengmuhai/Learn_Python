# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
msg = MIMEText('hello ,send by Python...', 'plain','utf-8')

#输入Email地址和口令
from_addr = 'fengmuhai@sina.com' #raw_input('From: ')
password = '1007682823fmh' #raw_input('Password: ')
#输入SMTP服务器地址
smtp_server = 'smtp.sina.com' #raw_input('SMTP Server: ')
#输入收件人地址
to_addr = ('1007682823@qq.com')#raw_input('To: ')

import smtplib
print '解析邮箱服务器地址...'
server = smtplib.SMTP(smtp_server,25) #SMTP协议默认端口是25
server.set_debuglevel(1)
print '邮箱验证中...'
server.login(from_addr, password)
print '邮件正在发送中...'
server.sendmail(from_addr, [to_addr], msg.as_string())
print '邮件发送成功！'
server.quit()