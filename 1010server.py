
# netstat -tanl 查看已经建立连接的网络
# netstat -tanl |grep 9999
# netstat -anp udp | grep 9999
# 查看占用9999端口的线程号 lsof -i:9999
# 结束线程 kill  线程号
# cat / etc / hosts mac查看本机IP








import socket
import selectors
import time
import logging
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(threadName)s %(thread)d %(message)s')


class ChatServer:
    def __init__(self, id='127.0.0.1', port=9999):
        self.addr = (id, port)
        self.sock = socket.socket()
        self.event = threading.Event()
        self.selector = selectors.DefaultSelector()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        self.sock.setblocking(False)

        key = self.selector.register(self.sock, selectors.EVENT_READ, data=self.accept)
        # print('key', key)
        # SelectorKey的多个属性中的4一个

        # SelectorKey(fileobj= < socket.socket fd = 3, type = SocketKind.SOCK_STREAM, laddr = ('127.0.0.1',9999) >,
        # fd = 3,
        # events = 1,
        # data = < bound method ChatServer.accept of <__main__.ChatServer object at 0x102e55438>>)

        threading.Thread(target=self.select, name='select').start()


    def select(self):
        while not self.event.is_set():
            events = self.selector.select()  # events是一个列表，第一个元素为一个元组（SelectorKey，mask）
            # 元组第一个参数为register返回值key
            # print('events:', events)
            for key, mask in events:
                # print('key in events:', key)
                # print('key.data:', key.data)  # ChatServer.accept函数
                callback = key.data   # callback函数分别是accept和recv函数
                callback(key.fileobj, mask)  # key.fileobj是返回的被包装的sock

    def accept(self, sock: socket.socket, *args):
        conn, raddr = sock.accept()  # 如果不发送消息则阻塞在self.selector.select()，收到消息后调用
        # callback()函数，即为调用accept函数，sock.accept()不阻塞。
        conn.setblocking(False)
        logging.info('new client socket {} in accept'.format(raddr))
        self.selector.register(conn, selectors.EVENT_READ, data=self.recv)

    def recv(self, conn: socket.socket, *args):
        data = conn.recv(1024)
        data = data.strip()
        if data == b'quit' or data == b' ':
            self.selector.unregister(conn)
            conn.close()
            return   # 因为只有一个线程，每一个注册都是调用一个新的函数，所以可以return

        msg = 'recv msg is {}'.format(data.decode())
        logging.info(msg)

        for key in self.selector.get_map().values():  # get_map  {'fd': SelectorKey},
            # SelectorKey有的是accept注册时返回的，有的是recv注册时返回的
            print('self.recv:', self.recv)
            print('key.data:', key.data)  # 第一次循环打印的key为，accept的SelectorKey，recv与
            # accept比较所以都为false
            print(self.recv is key.data)
            print(self.recv == key.data)
            if key.data == self.recv:
                key.fileobj.send(msg.encode())

    def stop(self):
        self.event.set()
        fobjs = []
        for fd, key in self.selector.get_map().items():
            fobjs.append(key.fileobj)
        for fobj in fobjs:
            self.selector.unregister(fobj)  # unregister的参数是sock
            fobj.close()
        self.selector.close()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input('>>')
        if cmd.strip() == 'quit':
            logging.info('quit')
            cs.stop()
            break
        print(threading.enumerate())



