import threading
import time

# tl = threading.local()

# tl.x = 'abc'
#
# def worker():
#     print('worker_dict', tl.)
#     tl.x += 'aaa'
#     print('{} {}'.format(threading.current_thread(), tl.x))
#
# t = threading.Thread(target=worker, name='woker')

# e = threading.Event()
# def boss(e:threading.Event):
#     time.sleep(5)
#     e.wait()  # if e: print('finish')
#     print('finish')
#





# import random
# import threading
# import logging
#
# class Dispatcher:
#     def __init__(self):
#         self.event = threading.Event()
#         self.c = threading.Condition
#
#     def produce(self, total):
#         logging.info('produce start')
#         for i in range(total):
#             with self.c:
#                 time.sleep(1)
#                 data = random.randint(1, 100)
#                 logging.info(data)
#                 self.data = data
#                 self.c.notify_all()
#
#     def consume(self):
#         logging.info('consume start')
#         while True:
#             with self.c:
#                 self.c.wait()
#                 print('consume {}'.format(self.data))
#
#
# d = Dispatcher()
# c = threading.Thread(target=d.produce, args=(10, ), name='consume')
# d = threading.Thread(target=d.consume, name='consume')
# c.start()
# d.start()
#
# class Conn:
#     def __init__(self, conn_name):
#         self.name = conn_name
#
#
# class Pool:
#     def __init__(self, maxsize=3):
#         self._max = maxsize
#         self._pool = []
#         self.sema = threading.BoundedSemaphore(maxsize)
#
#      def _connect(self, name):
#          return Conn(name)
#
#      def get_conn(self):
#          self.sema.acquire()
#          return self._pool.pop()
#
#      def return_conn(self, conn):
#          self._pool.append(conn)
#          # 先还再release(),因为还完了，准备就绪，才可以release
#          # 才可以恢复到原来的连接池数
#          self.sema.release()
#




# multiprocessing还提供共享内存、服务器进程来共享数据，还提供了用于进程间通讯的Queue队列、 Pipe管道
# 多进程就是启动多个解释器进程，进程间通信必须序列化、反序列化

# 进程池






















































