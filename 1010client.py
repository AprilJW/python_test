import threading
import logging
import datetime
import socket

logging.basicConfig(level=logging.INFO, format='%(threadName)s %(thread)d %(message)s ')


class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.addr)
        self.send("I'm ready")
        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)
            except Exception as e:
                logging.error(e)
                break
            if data == b'' or data == b'quit':
                self.sock.close()
                break
            print(data.decode())
            msg = '{:%Y/%m/%d %H:%M:%S} {} {} {}'.format(datetime.datetime.now(), *self.addr, data.decode())
            logging.info(msg)

    def send(self, msg:str):
        data = "{}\n".format(msg.strip()).encode()
        self.sock.send(data)

    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()
        logging.info('Clients stops.')


def main():
    cc = ChatClient()
    # cc = ChatClient('169.254.175.222', 9999)
    cc.start()
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            cc.stop()
            break
        cc.send(cmd)


if __name__ == '__main__':
    main()



