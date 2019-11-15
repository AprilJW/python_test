
# netstat tanl 查看已经建立连接的网络
# netstat tanl |grep 9999
# 查看占用9999端口的线程号 lsof -i:9999
# 结束线程 kill  线程号
# cat / etc / hosts mac查看本机IP

# import socket
# HOST = '127.0.0.1'
# PORT = 9999              # The same port as used by the server
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
# print('Received:', data.decode())


# import socket
#
# server = socket.socket()  #默认使用TCP协议，地址家族是IPV4
# addr = '127.0.0.1', 9999  # 字符串加整形组成元组，127.0.0.1，192.168.142.1, 172.16.250.198
# server.bind(addr)  # （ip, port） 套接字，只能绑定一次
# server.listen()  # 只能一次监听，监听所有服务端
# print(server)  # 这个socket包含，文件描述符和sever的ip及端口号
#
#
# print('begin accept')
# s1, info = server.accept()  # 阻塞
# # 同一个server可以接受2次及以上，因为一个服务端可以接受多个客户端的请求
# # s1  server中的第2个socket，包含文件描述符和sever的ip及端口号，还有client的ip和随机生成的无冲突的端口号
# # info  客户端口号和地址
# s1.recv(1024)  # 阻塞
#
# print(s1)
# print(info)
#
# s1.send('121212'.encode())  # 也可以阻塞
# s1.close()  # 归还文件描述符
# server.close()
# print('=======end=========')






