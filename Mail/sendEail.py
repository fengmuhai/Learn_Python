# -*- coding:utf-8 -*-

from email import encoders
from email.header import header
from eamil.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_ddr(s):
	name,addr = parseaddr(s)
	return formataddr((\
		Header(name,'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('to: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('hello, send by Python...','plain','utf-8')
msg['From'] = _format_addr(u'Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Suject'] = Header(u'来自SMTP的问候...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,[To], msg.as_string(0))
server,.quit()