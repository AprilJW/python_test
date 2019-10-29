
# class Node:
#     def __init__(self, value):
#         self.item = value
#         self.next = None
#         self.prev = None
#
#     def __str__(self):
#         return '<node item ={} = {} = {}>'.format(self.prev.item if self.prev else None,
#                                               self.item,
#                                               self.next.item if self.next else None)
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#
#     def append(self, value):
#         node = Node(value)
#         if self.head == None:
#             self.head = node
#             self.tail = node
#         else:
#             node.prev = self.tail
#             self.tail.next = node
#             self.tail = node
#         return self
#
#     def iterNode(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#
#     def remove(self, index):
#         if self.head == None:
#             raise Exception('Empty')
#
#         for i, node in enumerate(self.iterNode()):
#             if i == index:
#                 current = node
#                 break
#         else:
#             return 'index out of range'
#         if self.head == self.tail:
#             self.head = None
#             self.tail = None
#         else:
#
#             prev = current.prev
#             next = current.next
#
#             prev.next = next
#             next.prev = prev
#         return 'remove item {}'.format(current.item)
#
#
# l = LinkedList()
# l.append(1)
# l.append(2)
# l.append(3)
#
# for i in l.iterNode():
#     print(i)







# class Node:
#     def __init__(self, element, next=None):
#         self.element = element
#         self.next = next
#
#     def __str__(self):
#         return 'element is {} id is {}'.format(self.element, self.next)
#
#     __repr__ = __str__
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def lenght(self):
#         cur = self.head
#         if not cur:
#             return 0
#         count = 0
#         while cur:
#             cur = cur.next
#             count += 1
#         return count
#
#     def append(self, element):
#         node = Node(element)
#         if not self.head:
#             self.head = node
#         else:
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             cur.next = node
#
#     def add(self, element):
#         node = Node(element)
#         node.next = self.head
#         self.head = node
#
#     def insert(self, pos, element):
#         node = Node(element)
#         cur = self.head
#         if cur is None and pos == 0:
#             self.head = node
#         elif cur is not None and pos == 0:
#             self.add(node)
#         elif pos > self.lenght() - 1:
#             self.append(node)
#         else:
#             count = 1
#             while cur:
#                 if count >= pos:
#                     break
#                 cur = cur.next
#                 count += 1
#             node.next = cur.next
#             cur.next = node
#
#     def clear(self):
#         self.head = None
#
#     def remove(self, element):
#         if self.head is None:
#             return
#         cur = self.head
#         if cur.element == element:
#             self.head = cur.next
#             return 'remove element :{}'.format(element)
#         while cur:
#             try:
#                 if cur.next.element == element:
#                     cur.next = cur.next.next
#                     return 'remove element :{}'.format(element)
#                 cur = cur.next
#             except:
#                 return
#
#     def __iter__(self):
#         cur = self.head
#         while cur:
#             yield cur.element
#             cur = cur.next
#
#     def __add__(self, other):
#         self.append(other)
#         return self
#
#     def __len__(self):
#         return self.lenght()
#
#
#
# # linkedlist = LinkedList()
# #
# # linkedlist.append(5)
# # linkedlist.append(4)
# # linkedlist + 9 + 11 + 13
# # linkedlist.insert(1, 6)
# # for i in iter(linkedlist):
# #     print(i)
# #
# # print('lenght: ', len(linkedlist))
# # # print(linkedlist.remove(1))
#
#
# print('===============')
#
#
# # 双向链表
# class Node:
#     def __init__(self, element, next=None, prev=None):
#         self.element = element
#         self.next = next
#         self.prev = prev
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, element):
#         node = Node(element)
#         if self.head is None:
#             self.head = node
#         else:
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             cur.next = node
#             node.prev = cur
#
#     def pop(self):
#         cur = self.head
#         if cur is None:
#             return
#         elif cur.next is None:
#                 self.head = None
#                 return 'pop element is {}'.format(cur.element)
#         else:
#             while cur.next:
#                 cur = cur.next
#             cur.prev.next = None
#             return 'pop element is {}'.format(cur.element)
#
#     def __len__(self):
#         cur = self.head
#         count = 0
#         while cur:
#             cur = cur.next
#             count += 1
#         return count
#
#
#     def insert(self, pos, element):
#         node = Node(element)
#         cur = self.head
#         if cur is None:
#             self.head = node
#         else:
#             if pos == 0:
#                 node.next = cur
#                 node.next.prev = node   # 谁指向谁？？？？？？
#
#                 self.head = node
#
#             elif 0 < pos < len(self):
#                 count = 1
#                 while cur:
#                     if count >= pos:
#                         break
#                     cur = cur.next
#                     count += 1
#                 node.next = cur.next
#                 node.next.prev = node
#                 node.prev = cur
#                 cur.next = node
#
#             else:
#                 self.append(element)
#
#     def remove(self, element):
#         if self.head is None:
#             return
#         cur = self.head
#         if cur.element == element:
#             self.head = cur.next
#             if cur.next is not None:
#                 cur.next.prev = None
#             return 'remove element is {}'.format(element)
#         cur = cur.next
#         if cur is not None:
#             while cur.next:
#                 if cur.element == element:
#                     cur.prev.next = cur.next
#                     cur.prev = cur.next.prev
#                     return 'remove element is {}'.format(element)
#                 cur = cur.next
#             else:
#                 if cur.element == element:
#                     cur.prev.next = None
#                     return 'remove element is {}'.format(element)
#
#     def make_key(self):
#         items = {}
#         cur = self.head
#         while cur:
#             items[cur.element] = items.getitem(cur.element, 0) + 1
#             cur = cur.next
#         return items
#
#     def __iter__(self):
#         cur = self.head
#         while cur:
#             yield cur.element
#             cur = cur.next
#
#     def __getitem__(self, item):
#         num = self.make_key().getitems(item, None)
#         return 'The num of {} is {}'.format(item, num)
#
#     def __setitem__(self, key, value):
#         self.make_key()[key] = value
#         return '{} : {}'.format(key, value)
#
# d = DoubleLinkedList()
# d.append(1)
# d.append(55)
# d.insert(0, 9)
# d.insert(1, 8)
# d.insert(99, 10)
# d.append(100)
# #print(d.pop())
# print(d.remove(100))
#
# for i in iter(d):
#     print(i)

# 容器实现链表


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None

    def __str__(self):
        # return 'node {} <== node {} ==> node {}'.format(self.prev, self.elem, self.next)
        # self.prev和self.next都是都是指向节点，如果是有2个及以上元素的链表，则会产生递归
        # return '{}'.format(self)
        # return str(self)
        return ' {} <==  {} ==>  {}'.format(self.prev.elem if self.prev else None,
                                          self.elem,
                                          self.next.elem if self.next else None)
    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __getitem__(self, index):
        if index >= self._size or index < -self.size:
            if self._size == 0:
                raise Exception('empty link_list')
            raise IndexError('index out of range')
        edge = index if index >= 0 else self._size + index -1
        current = self.head
        for i in range(edge):
            current = current.next
        #     print('inter:', current)
        # print('current:', current)
        return current

    def __setitem__(self, index, elem):
        self[index].elem = elem
        return elem

    def append(self, elem):
        node = Node(elem)
        if self.head is None:
            self.head = node
        else:
            current = self.tail
            node.prev = current
            current.next = node
        self.tail = node
        self._size += 1
        return self

    def insert(self, index, elem):
        # print('self._size:', self._size)
        if index >= self._size:
            # print('append append')
            self.append(elem)
            # print('self.tail:', self.tail)
            return elem

        if index < -self._size:
            index = 0

        current = self[index]

        node = Node(elem)
        prev = current.prev
        next = current

        if prev is None:
            self.head = node
        else:
            node.prev = prev
            prev.next = node
        node.next = next
        next.prev = node

        self._size += 1
        #print('self.tail:', self.tail)
        return elem

    def pop(self):
        if self.head is None:
            raise Exception('empty link_list')

        node = self.tail
        prev = node.prev
        elem = node.elem

        if prev is None:
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev

        self._size -= 1
        return elem


    def remove(self, index):
        pass




    def iter_items(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def __iter__(self):
        yield from self.iter_items()

    size = property(lambda self: self._size)



link_list = LinkedList()
#link_list.append(5).append(6).append(7)
# # print(link_list[0])
# print(link_list[-1])
# print(link_list[-3])
# #print(link_list[-9])
# print(link_list[0])
# print(link_list[1])
# print(link_list[2])
# #print(link_list[9])
# #print(link_list.size)
# # link_list.size = 90
print(link_list._size)
print('*****')
print(link_list.insert(0, 9))
print(link_list.insert(1, 9))
print(link_list.insert(4, 44))
print(link_list.insert(10, 100000))
print(link_list.insert(-1, 100))
print(link_list.insert(-8, 300))
print(link_list.insert(-100, 200))


for n in link_list:
    print(n)
#
# for n in link_list.iter_items(True):
#     print(n)






