# -*- coding:utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
sock.connect(('127.0.0.1', 9999))
#接受欢迎消息
print sock.recv(1024)
for data in ['Micheal','Tracy','Sarah']:
	#发送消息
	sock.send(data)
	print sock.recv(1024)

sock.send('exit')
sock.close()
