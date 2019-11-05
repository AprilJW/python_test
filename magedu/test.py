class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __add__(self, other):
        self.next = other
        return other

class LinkList:
    def __init__(self):
        self.head = None

    def __add__(self, other):
        if hasattr(self, 'head'):
            self.head = other
        return other

    def __getitem__(self, index):
        if hasattr(self, 'head'):
            p = self.head
        j = 0
        while p:
            if j == index:
                return p.elem
            p = p.next
            j += 1
        raise IndexError('index out of range')

    def insert(self, i, elem):
        node = Node(elem)
        p = self.head
        if i == 0 and p == None:
            self.head = node
            return elem
        if i == 0:
            node.next = self.head
            self.head = node
            return elem
        j = 0
        while p:
            if j == i-1:
                node.next = p.next
                p.next = node
                return elem
            p = p.next
            j += 1

# list.insert()
#
# l = LinkList()
# l + Node(21) + Node(18) + Node(30) + Node(56)
# print(l[0])
# print(l[2])
# print(l[3])
# #print(l[8])


# 参数检查
# 装饰器，使用inspect模块完成


# 加入描述器，实例属性访问顺序




# class Person:
#     def __init__(self, first_name):
#         print('1')
#         self.first_name = first_name
#         print('3')
#
#     def get_first_name(self):
#         return self._first_name
#
#     def set_first_name(self, first_name):
#         print('2')
#         if not isinstance(first_name, str):
#             raise TypeError('Expected a string')
#         self._first_name = first_name
#
#     name = property(get_first_name, set_first_name, doc='add Property')
#
#
# p = Person('tom')
# # p = Person(10)
# # print(p.__dict__)
# # print(p.first_name)
# # p.first_name = 'jerry'
# # print(p.first_name)


import sys

# print(os.stat('/Users/jw/Projects/Mask_RCNN'))

# print(sys.modules.keys())
# import test1







# 无参构造与值
# import test1
# print(sys.modules.keys())
# print(sys.path)
# print(__name__.__modules__)
# import test1

# import os.path

import os
print(os.path)
















#






























