# 8.1
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        print('repr')
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        print('str')
        return 'Pair({!s}, {!s})'.format(self.x, self.y)

    #__repr__ = __str__

# p = Pair(1, 2)
# print('{}'.format(p))
# print('{!s}'.format(p))

#8.3
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None
        return True

# from functools import partial, wraps
#
# conn = LazyConnection(('www.python.org', 80))
# with conn as s:
#     s.send(b'GET /indes.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv, 1), b''))
#     print('456')
#     #raise Exception('123')
#     print('resp', resp)
#
# def add(x, y):
#     return x + y
# print(partial(add, 1)(3))
#
# def a(cls):
#     print(cls.__name__)
#     return 123
#
# def b():
#     return partial(a, int)
# print(b()())
#
# def wraps1(fn):
#     return partial(update_wrapper1, wrapperd=fn)
#
# def update_wrapper1(wrapper, wrapperd):
#     print(wrapper)
#     print(wrapperd)
#
# print(wraps1(1)(2))
# wraps(add)(a)
# print(a.__name__)
#
# import random
# for i in iter(partial(random.randint, 1, 5), 5):
#     print('*****')
#     print(i)
#
# a = partial(random.randint, 1, 5)
# print('a:', a())

# 8.5
class A:
    def __init__(self):
        self.__private = 0
        self._internal = 1
    def __private_method(self):
        pass

    def _internal_method(self):
        pass

a = A()
print(a.__dict__)
print(A.__dict__)