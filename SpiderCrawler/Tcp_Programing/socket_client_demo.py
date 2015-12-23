# -*- coding:utf-8 -*-
#导入socket库
import socket

#创建socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#建立连接
sk.connect(('www.sina.com.cn',80))

# 发送数据:
sk.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
	#每次最多接收1024个字节
	d = sk.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)

#关闭连接
sk.close()

header, html = data.split('\r\n\r\n',1)
print header

with open('sina.htm', 'wb') as f:
	f.write(html)
