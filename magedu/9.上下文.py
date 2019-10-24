import time
import datetime

def timeit(add):
    def wrapper(x, y):
        t1 = datetime.datetime.now()
        result = add(x, y)
        delta = (datetime.datetime.now() - t1).total_seconds()
        print(delta)
        return result
    return wrapper


@timeit  #add = wrapper(add)
def add(x, y):
    #time.sleep(2)
    return x + y

#

# class TimeIt:
#     def __init__(self, obj):
#         self.obj = obj
#
#         #self.calulatetime(obj)
#
#     def calulatetime(self, obj):
#         t1 = time.time()
#         print(obj(1, 2))
#         return time.time() - t1
#
#
#     def __enter__(self):
#         return self.calulatetime(self.obj)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
# with TimeIt(add) as t:
#     print(t)


# 方法1
class TimeIt:
    def __init__(self, obj=None):
        self.obj = obj

    def __enter__(self):
        self.start = datetime.datetime.now()
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print('time:', delta)

# with TimeIt(add):
#     add(1, 2)

#print('class decorate')
# 通过类装饰器实现
from functools import update_wrapper, wraps
class TimeIt:
    """
    122234
    """
    def __init__(self, fn):
        self.fn = fn
        # self.__name__ = fn.__name__
        # self.__doc__ = fn.__doc__
        # update_wrapper(self, fn)
        wraps(fn)(self)


    def __call__(self, *args, **kwargs):
        ret = self.fn(*args, **kwargs)
        print(ret, self.__name__, self.__doc__)
        return ret


@TimeIt  # add = TimeIt(add)
def add(x, y):
    """ doc add"""
    #time.sleep(2)
    return x + y

#print(add(1, 2))


# 魔术方法都是存在类的字典中，属于类的方法
# 实例调用类的方法，实例会作为第一参数注入
# 实例调用实例的方法，实例不会作为第一参数注入（无bound）
# 实例的方法，不可以被类的调用

#


# l
# f = open("/Users/jw/PycharmProjects/python_test/magedu/9.上下文.py", encoding='utf8')
# with f as p:
#     print(f is p)  # True
#     print(f == p)  # False




#
# class Point:
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#         return self  # 添加返回值
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('1')
#         return 123
#
#
# p = Point()
# with p as f:
#     raise Exception('Error')
#     print('2')



# class TimeIt:
#   def __init__(self, fn):
#     self.fn = fn
#
#   def __call__(self, x, y):
#       start = datetime.datetime.now()
#       ret = self.fn(x, y)
#       print((datetime.datetime.now() - start).total_seconds())
#       return ret
#
# @TimeIt # add = TimeTt(add)
# def add(x, y):
#   #time.sleep(2)
#   return x + y
#
# print(add(1, 2))




# from functools import wraps, update_wrapper
# import time
# import datetime
# def timeit(fn):
#       #@wraps(fn) #wraps(fn)(wrapper)
#       def wrapper(*args, **kwargs):
#           start = datetime.datetime.now()
#           ret = fn(*args, **kwargs)
#           delta = (datetime.datetime.now() - start).total_seconds()
#           update_wrapper(wrapper, fn)
#           print(fn.__name__, delta)
#           return ret
#       return wrapper
#
# @timeit
# def add(x, y):
#   # time.sleep(2)
#   return x + y
#
# print(add(1, 2))

















































































































