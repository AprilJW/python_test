# import base64
#
# # x = str(123)
# # def revert(src:str, target=[]):
# #     if src:
# #         target.append(src[-1])
# #         revert(src[:-1], target)
# #     return target
# #
# # print(revert(x))
#
#
#
# # print(revert(x))
# # #print(revert(x))
# #
# # from functools import wraps
# # import re
# # a = re.findall()
# import random
#
# #nums = [random.randint(0, 20) for i in range(4)]
# #print(nums)
#
#
# # def merge_sort(alist):
# #     if len(alist) <= 1:
# #         return alist
# #     # 二分分解
# #     num = len(alist)//2
# #     left = merge_sort(alist[:num])
# #     right = merge_sort(alist[num:])
# #     # 合并
# #     return merge(left, right)
# #
# # def merge(left, right):
# #     '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
# #     #left与right的下标指针
# #     l, r = 0, 0
# #     result = []
# #     while l<len(left) and r<len(right):
# #         if left[l] < right[r]:
# #             result.append(left[l])
# #             l += 1
# #         else:
# #             result.append(right[r])
# #             r += 1
# #     result += left[l:]
# #     result += right[r:]
# #     return result
# #
# # nums = [54, 26, 93, 17]
# # # sorted_alist = merge_sort(nums)
# # # print(sorted_alist)
# #
# # import re
# #
# # s = '''bottle\nbag\nbig\napple'''
# # pattern = '[\w\n]+'
# # regex = re.compile(pattern)
# # print(regex)
# #re.fullmatch()
#
# # import os
# # from os import path
# # import re
# #
# # p = path.join('a', 'b', 'c')
# # print(p)
# # print(re.split(r'/', p))
# # p = r'/etc/windows/nt'
# # # 在mac中如果路径中有\，则会被自动转成\\
# # print(re.split(r'[\\/]', p))
# # print(path.split(p))  #('/etc/windows', 'nt')
# # print(path.basename(p))  #nt
# # print(path.dirname(p)) #/etc/windows
# # print('********')
# # # 在windows下面使用，返回一个二元组，第一个参数是驱动，例如'c:\'
# # print(path.splitdrive(p)) #('', '/etc/windows/nt')
# # print(path.splitdrive('etc/windows/nt')) #('', 'etc/windows/nt')
# # print(path.splitdrive("//host/computer/dir")) #官方给的例子，在mac上不能产生预期的结果
# #
# # #  切出最后一个点后面的后缀
# # print(path.splitext('/etc/windows/nt')) #('/etc/windows/nt', '')
# # print(path.splitext('/etc/windows/nt.py')) #('/etc/windows/nt', '.py')
# # print(path.splitext('/etc/windows/nt.cn.com')) #('/etc/windows/nt.cn', '.com')
# #
# # print(path.abspath(p)) #/etc/windows/nt
# # print(path.curdir) #.
# # print(path.dirname(p)) #/etc/windows
# # print(path.exists(p)) #p只是一个字符串不是一个路径，返回fasle
# # print(path.exists('/Users/jw/anaconda3')) #这是一个系统路径返回True
# # print(path.exists('/Users/jw/PycharmProjects/python_test' + p)) #False
# # print(os.environ['PATH']) #获得系统路径
# # print(os.getcwd()) #获得当前test文件的路径
# # print(path.getatime('prog.py')) #filename只能是 当前路径 下面的文件
# # print(path.getatime('test.txt'))
# # print(path.getatime('/Users/jw/Projects/test1/manage.py')) #或者filename给绝对路径
# # print(path.getmtime('prog.py'))
# # print(path.getctime('prog.py'))
# # print(path.getsize('prog.py')) #获得filename大小
# # print(path.isabs(r'etc/windows/nt')) #r'/etc/windows/nt' 是绝对路径，r'etc/windows/nt' 不是绝对路径
# # print(path.isabs('/Users/jw/Projects/test1/manage.py'))
# # print(path.isfile(r'etc/windows/nt'))
# # print(path.islink(r'etc/windows/nt'))
# # print(path.join('/Users', 'wj', 'Projects/python_test', 'kk'))
# # print(path.join(b'bytes1', b'bytes2'))
# # # join后面的路径不能出现斜杠/，否则前面的路径都没有
# # # union
# # # 里面的内容可以是，str, PathLike,两者也可以结合使用
# # # 如果里面的是bytes，则只能是bytes
# #
# #
# # from pathlib import Path
# # p = 'etc/sysconfig/network-scripts'
# # print(Path(p), str(Path(p)), type(Path(p))) #<class 'pathlib.PosixPath'>
# # # 将类变成字符串  str(Path(p))
# # print(Path(p, 'a', 'b/c')) #etc/sysconfig/network-scripts/a/b/c
# # print(Path(p, 'a', 'b/c', s='d')) # ?????????
# # path1 = Path(p, 'a', 'b/c')
# # print(path1.parts) #('etc', 'sysconfig', 'network-scripts', 'a', 'b', 'c')
# # #print(path1.absolute(), path1.absolute('.')) #??????
# # print(path1.absolute()) #/Users/jw/PycharmProjects/python_test/etc/sysconfig/network-scripts/a/b/c
# # print(path.abspath('etc/windows/nt')) #/Users/jw/PycharmProjects/python_test/etc/windows/nt
# # print(path.abspath(path1)) #/Users/jw/PycharmProjects/python_test/etc/sysconfig/network-scripts/a/b/c
# #
# # print(path.abspath(''), path.abspath('.')) #/Users/jw/PycharmProjects/python_test
# # print(Path(), Path(''), Path('.')) #都返回当前，一个点 ??????????????
# # print(os.getcwd()) #/Users/jw/PycharmProjects/python_test
# #
# # path2 = path1 / 'a' / 'a/c/d' #Path对只能放在前两个位置, 不拼出来的是相对路径
# # path2 = 'a'/ path1 / 'a/c/d'
# # path2 = Path() / 'a' / 'b'
# # print(path2)
# # print(path2.absolute()) #/Users/jw/PycharmProjects/python_test/a/b
# # print((Path() / 'a' / 'b').absolute())
# # print(Path().joinpath('a', 'b').absolute())
# #
# # path3 = Path().joinpath('a', 'b').absolute()
# # print(path3.parents) #<PosixPath.parents>
# # for i in path3.parents:
# #     print(i)
# #     #path3=/Users/jw/PycharmProjects/python_test/a/b
# #     #path3 的parents分别是/Users/jw/PycharmProjects/python_test/a 到/
# # print(path3.parents[0]) #/Users/jw/PycharmProjects/python_test/a
# # print(path3.parent) #/Users/jw/PycharmProjects/python_test/a
# # print(path3.name) #b
# #
# # path1 = Path() / '/Users/jw/PycharmProjects/python_test/a.com.cn.dd'
# # print(path1)
# # print(path1.suffix) #.dd
# # print(path1.suffixes) #['.com', '.cn', '.dd']
# # print(path1.stem) #a.com.cn 会少一个.dd
# # print(path.basename(path1)) #a.com.cn.dd
# #
# # print(path1.with_suffix('.tar'))#/Users/jw/PycharmProjects/python_test/a.com.cn.tar
# # print(path1.with_name('.tar'))
# # print(path1.with_name('yyyy')) #将a.com.cn.tar替换成了yyy/Users/jw/PycharmProjects/python_test/yyyy
# #
# # print(path1.home()) #获得家目录
# # print(Path().home())
# #
# # path1.is_block_device()
# # path1.is_char_device()
# # path1.is_dir()
# # path1.is_fifo()
# # path1.is_file()
# # path1.is_socket()
# # path1.is_symlink()
# #
# # print(Path('stdout').absolute())
# # print(Path('stdout').resolve()) #变成绝对路径，并解决软连接问题和斜杠问题
# #
# # #遍历目录下的文件，文件夹，文件夹如果不为空打印
# # for f in  p4.parents[len(p4.parents)-2].iterdir():
# #     if f.is_dir():
# #         flag = False
# #         for x in f.iterdir:
# #             flag = True
# #             break
# #         print('dir\t\t{}\t{}'.format(str(f), 'Not Empty' if flag else 'Empty'))
# #     elif f.is_file():
# #         print('file\t\t{}\t{}'.format(str(f)))
# #     else:
# #         print('other file\t\t{}'.format(str(f)))
# #
# # #用python建立多级目录
# # p5 = Path('/Users/jw/Projects/a/b/c/d')
# # p5.parent.mkdir(parents=True, exist_ok=True)
# # with p5.open('a') as f:
# #     f.write('abcde\nxyz')
# #
# # import shutil
# # src = Path('/Users/jw/Projects/a.txt')
# # dst = Path('/Users/jw/Projexts/a.txt.bak')
# # with src.open('rb') as fsrc:
# #     with dst.open('wb') as fdst:
# #         shutil.copyfileobj(fsrc, fdst, length=0) # 拷贝fileobject
# #
# # def ignore(src, names) -> set:
# #     s = set()
# #     for name in names:
# #         if name.startswith('1'):
# #             s.add(name)
# #     return {name for name in names if name.startswith('1')}
# #     #return set(filter(lambda name: name.startswith, names))
# #
# # #要求目标路径不存在
# # shutil.copytree('/Users/jw/Projects/a', '/Users/jw/Projects/b', ignore=ignore)
# # #同时拷贝文件内容，和filemode
# # shutil.copy()
# # #同时拷贝文件内容，和filemode,filestat
# # shutil.copy2()
# #
# # shutil.copyfileobj()
# # shutil.copyfile()
# # from m import *
# # from m import *
# # print(A)
# # print(m11._B)
# # print(x)
#
#
#
#
#
#
#
# # import logging
# # FORMAT = '%(asctime)-15s\nThread info: %(thread)d %(threadName)s %(message)s'
# # logging.basicConfig(format=FORMAT, level=logging.WARNING, datefmt='%Y-%m-%d %H:%M:%S', filename='test.log')
# # logging.warning('I am {}'.format(20))
#
#
#
#
#
#
#
# #
# #

import logging
import socket
import threading
import datetime


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(thread)d %(threadName)s %(message)s')

class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.clients = {}  # 因为后面涉及到删除所以用字典，没用列表
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        # 因为accept会阻塞当前主线程所以再开一个线程
        threading.Thread(target=self.accept).start()

    def accept(self):  # 等待多个客户端
        while not self.event.is_set():
            sock, client = self.sock.accept()  # 等待客户端响应，阻塞每一个客户端线程
            self.clients[client] = sock  # client是一个元组，而且元组内部可哈希
            # logging.info('{} {}'.format(*client))
            threading.Thread(target=self.recv, args=(sock, client)).start()

    def recv(self, sock, client):  # 等待一个客户端发送数据
        while not self.event.is_set():
            print('*********')
            data = sock.recv(1024)  # 阻塞当前客户端，发送数据的线程
            msg = '{} {} {}'.format(*client, data.decode())
            logging.info(msg)
            msg = msg.encode()
            for s in self.clients.values():
                s.send(msg)

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.socket.close()


cs = ChatServer()
cs.start()


# 解决客户端断开，服务器删除self.client字典










