# 容器实现单向链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return 'node: {}'.format(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return self
        self.tail.next = node
        self.tail = node
        return self

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __len__(self):
        for i, _ in enumerate(self):
            pass
        return i + 1


ll = LinkedList()
ll.append(1).append(2).append(3).append(4).append(5).append(6).append(7)

# for i in ll:
#     print(i)
#
# print(len(ll))



# 容器实现双向链表


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


class DoubleLinked:
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
        if index < -self._size or index >= self._size:
            if self._size == 0:
                raise Exception('empty')
            raise IndexError('index out of range')

        current = self[index]
        next = current.next
        prev = current.prev

        if current == self.tail:
            self.pop()
        elif current == self.head:
            self.head = next
            next.prev = None
            self._size -= 1
        else:
            next.prev = prev
            prev.next = next
            self._size -= 1
        return current.elem

    def iter_items(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def __iter__(self):
        yield from self.iter_items()

    size = property(lambda self: self._size)

    def removedupli(self):
        # if self.head is None:
        #     return self.head
        #
        # cur = self.head
        # pos1 = cur.next
        #
        # while cur is not None and pos1 is not None:
        #     if cur.elem == pos1.elem:
        #         pos1 = pos1.next
        #     else:
        #         cur.next = pos1
        #         pos1.pre = cur
        #         cur = pos1
        #         pos1 = pos1.next
        # cur.next = None
        # self.tail = cur
        # return self.tail
        cur = self.head
        while cur is not None and cur.next is not None:
            if cur.elem == cur.next.elem:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.head


b = DoubleLinked()
b.append(1).append(1).append(2).append(3).append(3)
# b.append(1).append(1).append(2)
# print('************')
# for n in b:
#     print(n)

# b.removedupli()






# link_list = LinkedList()
# #link_list.append(5).append(6).append(7)
# # # print(link_list[0])
# # print(link_list[-1])
# # print(link_list[-3])
# # #print(link_list[-9])
# # print(link_list[0])
# # print(link_list[1])
# # print(link_list[2])
# # #print(link_list[9])
# # #print(link_list.size)
# # # link_list.size = 90
# print(link_list._size)
# print('*****')
# print(link_list.insert(0, 9))
# print(link_list.insert(1, 9))
# print(link_list.insert(4, 44))
# print(link_list.insert(10, 100000))
# print(link_list.insert(-1, 100))
# print(link_list.insert(-8, 300))
# print(link_list.insert(-100, 200))
#
#
#
#
# for n in link_list:
#     print(n)
#
# print('*********')
# print(link_list.remove(0))
# print(link_list.remove(5))
# print(link_list.remove(3))
# print(link_list.remove(-1))
# print(link_list.remove(-3))
# print(link_list.remove(-2))
# # print(link_list.remove(8))
# print(link_list.remove(0))
# # print(link_list.remove(0))
# # print(link_list.remove(-9))
#
# print('***********')
# for n in link_list:
#     print(n)
#
# # for n in link_list.iter_items(True):
# #     print(n)








