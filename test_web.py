#-*-coding: UTF-8 -*-
#CS,软件主要运行在桌面，而数据库这样的软件运行在服务器
#这种客户/服务（client/server）模式简称CS架构。
#Web应用程序的修改和升级非常迅速，而CS架构需要每个客户端逐个升级桌面App，
#因此，Browser/Server模式开始流行，简称BS架构。
# import os
# def set_env():
#     os.environ.setdefault('test', '2')
#     return os.environ
#
# def get_env():
#     if os.environ.get('test'):
#         print(os.environ['test'])
#     else:
#         print(None)
#
# def del_env():
#     del os.environ['test']
# print(set_env())
# get_env()
# del_env()
# get_env()
# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return'<h1>Home</h1>'
#
# @app.route('/sigin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
#
# if __name__=='__main__':
#     app.run()
#为了把全世界所有不同类型的计算机连接起来，需要遵循互联网协议（TCP/IP）
# 互联网上每台计算机的唯一标识就是IP地址，实际上是计算机的网络接口
# 通常指网卡，IP协议负责把数据从一台电脑发送到另一台电脑，数据被分成一小块
# 然后通过IP包转发出去，但不能保证到达，IP地址实际是一个32位的整数（IPv）
# 把32位的整数按8位分组后的数字表示192.168.0.1。IPv6地址实际是一个128位
# 整数。TCP协议可以保证数据包按顺序到达。HTTP是用于浏览器的协议，是建立在
# TCP协议基础上的，一个TCP报文包含传输数据，源IP地址，目标IP地址，
# 源端口和目标端口
# 一个Socket通常表示打开一个网络链接，这时需要目标计算机的IP地址和端口号
# 再指定协议类型即可。
# import socket
#
# #SOCK_STREAM指定使用面向流的TCP协议, socket.AF_INET指IPv4协议
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接:
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()