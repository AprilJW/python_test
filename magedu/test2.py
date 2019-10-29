import test1
import sys

# print(sys.path)
print('*****')
# import test1  # 只能看到一次1，2，3， 4的打印，只有第一次打印了，

# print(sys.modules.keys())  # 可以看到test1在里面了。
# print(test1.__dict__.keys())
# print('__main__'.__dict__)
# import os
# from os.path import exists
# print(os.path.exists)
# print(exists)
# print(os.path.__dict__['exists'])  # 字符串
# print(getattr(os.path, 'exists'))  # 字符串
# print(type(os.path))

from functools import wraps as wr, partial
# print(dir())  # [..., 'wr', 'partial']

def testimport():
    import os.path
    print(dir())  # os存在里面
    print(globals().keys())  # os不存在里面
    print(locals().keys())

testimport()
print('#########')
print(globals().keys())  # os不存在里面
print(locals().keys())