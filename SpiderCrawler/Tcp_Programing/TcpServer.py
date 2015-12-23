# -*- coding:utf-8 -*-
import socket
import threading
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
sock.bind(('127.0.0.1',9999))
#调用listen监听端口，传入参数为最大客户端连接数
sock.listen(5)
print 'listen to connect...'

def tcplink(sk,addr):
	print 'Accept new connection from %s:%s...' % addr
	sk.send('Welcome ')
	while True:
		data = sk.recv(1024)
		time.sleep(1)
		if data=='exit' or not data:
			break
		sk.send('Hello %s!' % data)
	sk.close()
	print 'Connection from %s:%s closed!' % addr


#循环等待客户端连接
while True:
	#接受一个新的请求
	sk, addr = sock.accept()
	#创建一个新的线程来处理TCP连接
	t = threading.Thread(target=tcplink,args=(sk,addr))
	t.start()

