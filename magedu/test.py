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

class StaticMethod:

    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn


from functools import partial
class ClassMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return partial(self.fn, owner)


class A:
    @StaticMethod
    def f1(x, y):
        print(x + y)

    @ClassMethod
    def f2(cls):
        print(cls.__name__)

a = A()
a.f1(4, 5)

print(a.f2)
print(a.f2())

# 参数检查
# 1。 2装饰器 3。miaoshu


