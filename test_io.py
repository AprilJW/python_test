#-*-coding: UTF-8 -*-

# try:
#     f = open(r'/Users/jw/Projects/python/python_duoduo/20190428_python.txt',
#              'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# with open(r'/Users/jw/Projects/python/python_duoduo/20190428_python.txt', 'r') as f:
#     print(f.read())
#
# with open(r'/Users/jw/Projects/python/python_duoduo/20190428_python.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())
#为什会乱码？
# with open(r'/Users/jw/Projects/python/python_duoduo/test.jpg', 'rb') as f:
#     print(f.read())

# with open(r'/Users/jw/Projects/python/python_duoduo/20190428_python.txt', 'a') as f:
#     f.write('Hello world ')
#     #print(f.read())
#
# with open(r'/Users/jw/Projects/python/python_duoduo/20190428_python.txt', 'r') as f:
#     print(f.read())

import os
from copy import deepcopy

# print(os.path.abspath('.'))
# a = os.path.join(r'/Users/jw/Projects/python/python_duoduo/', '20190428_python_new.txt')
# print(a)
#os.mkdir(a)
#os.rmdir(a)
# print(os.path.split(a))
# print(os.path.splitext(a))
# b = deepcopy('/Users/jw/Projects/python/python_duoduo/20190428_python_123.txt')
# os.rename(b, '/Users/jw/Projects/python/python_duoduo/20190428_python_345.txt')

# from shutil import copyfile
# copyfile(r'/Users/jw/Projects/python/python_duoduo/20190428_python_345.txt',
#          '/Users/jw/Projects/python/python_duoduo/20190428_python_789.txt')

# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and
#        os.path.splitext(x)[1] == '.py'])

#把变量从内存中变成可存储和传输的过程称为序列化（pickling）,
#序列化之后可以把内容写入磁盘
#把序列化的对象重新读取到内存称为反序列化（unpickling）
import json
import yaml
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# with open('/Users/jw/Projects/python/python_duoduo/20190428_python_789.txt', 'w') as f:
#     d = dict(name='Tom', age='25', score='90')
#     e = json.dumps(d)
#     f.write(e)
#
# with open('/Users/jw/Projects/python/python_duoduo/20190428_python_789.txt', 'r') as f:
#     g = f.read()
#     print(g)
#     print(type(g))
#     #h = json.loads(g)
#     h = yaml.load(g)
#     print(h)
#     print(type(h))

# with open(r'/Users/jw/Projects/python/python_duoduo/20190428_python_789.txt', 'r') as f:
#     print(f.read())
#
# with open(r'/Users/jw/Projects/python/python_duoduo/20190428_python_789.txt', 'a') as f:
#     print(f.write('hello'))

# with open(r'/Users/jw/Projects/python/python_duoduo/20180428_python_789.txt', 'a') as f:
#     a = list([1, 2, 3, 4])
#     f.write(json.dumps(a))
#
# with open(r'/Users/jw/Projects/python/python_duoduo/20180428_python_789.txt', 'r') as f:
#     a = f.read()
#     print(a, type(a))
#     print(yaml.load(a),type(yaml.load(a)))

# with open(r'/Users/jw/Projects/python/python_duoduo/test_json.json', 'w') as f:
#     dict1 = {1: 'a', 2: 'b', 3: 'c'}
#     f.write(json.dumps(dict1))
#
# with open(r'/Users/jw/Projects/python/python_duoduo/test_json.json', 'r') as f:
#     a = f.read()
#     print(yaml.load(a), type(yaml.load(a)))

# a = [1,2,1,3]
# b = list(set(a))
# a = 'abc'.reverse()
# print(a)
# reversed('abc')

import csv
rows = [
    ['c', 'd'],
    ('e', 'f'),
    'ab'
]


with open('nfile', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open('nfile', encoding='utf8') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)

import configparser
from pathlib import Path

#p1 = Path(__file__).with_name('cfg.ini') __file__只在pycharm中可以用
p1 = '/Users/jw/Projects/python23/magedu/python/cfp.ini'

cfp = configparser.ConfigParser()
oks = cfp.read(p1)
print(type(oks), oks) #读取成功的文件都放一个列表里
print(cfp.sections()) #['mysql', 'mysqld']除了DEFAULT的sections的部分
print(cfp._sections) # 不包含DEFAULT的部分
# OrderedDict([('mysql', OrderedDict([('default-character-set', 'utf8')])), ('mysqld', OrderedDict([('port', '33060'), ('character-set-server', 'utf8')]))])
print(cfp.default_section) #DEFAULT
print(cfp.defaults()) #OrderedDict([('a', 'test')])
print(cfp._defaults) #一般不用
