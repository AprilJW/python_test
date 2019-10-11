class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return 'element is {} id is {}'.format(self.element, self.next)

    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head = None

    def lenght(self):
        cur = self.head
        if not cur:
            return 0
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def append(self, element):
        node = Node(element)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def add(self, element):
        node = Node(element)
        node.next = self.head
        self.head = node

    def insert(self, pos, element):
        node = Node(element)
        cur = self.head
        if cur is None and pos == 0:
            self.head = node
        elif cur is not None and pos == 0:
            self.add(node)
        elif pos > self.lenght() - 1:
            self.append(node)
        else:
            count = 1
            while cur:
                if count >= pos:
                    break
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def clear(self):
        self.head = None

    def remove(self, element):
        if self.head is None:
            return
        cur = self.head
        if cur.element == element:
            self.head = cur.next
            return 'remove element :{}'.format(element)
        while cur:
            try:
                if cur.next.element == element:
                    cur.next = cur.next.next
                    return 'remove element :{}'.format(element)
                cur = cur.next
            except:
                return

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.element
            cur = cur.next

    def __add__(self, other):
        self.append(other)
        return self

    def __len__(self):
        return self.lenght()



# linkedlist = LinkedList()
#
# linkedlist.append(5)
# linkedlist.append(4)
# linkedlist + 9 + 11 + 13
# linkedlist.insert(1, 6)
# for i in iter(linkedlist):
#     print(i)
#
# print('lenght: ', len(linkedlist))
# # print(linkedlist.remove(1))


print('===============')


# 双向链表
class Node:
    def __init__(self, element, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def pop(self):
        cur = self.head
        if cur is None:
            return
        elif cur.next is None:
                self.head = None
                return 'pop element is {}'.format(cur.element)
        else:
            while cur.next:
                cur = cur.next
            cur.prev.next = None
            return 'pop element is {}'.format(cur.element)

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count


    def insert(self, pos, element):
        node = Node(element)
        cur = self.head
        if cur is None:
            self.head = node
        else:
            if pos == 0:
                node.next = cur
                node.next.prev = node   # 谁指向谁？？？？？？

                self.head = node

            elif 0 < pos < len(self):
                count = 1
                while cur:
                    if count >= pos:
                        break
                    cur = cur.next
                    count += 1
                node.next = cur.next
                node.next.prev = node
                node.prev = cur
                cur.next = node

            else:
                self.append(element)

    def remove(self, element):
        if self.head is None:
            return
        cur = self.head
        if cur.element == element:
            self.head = cur.next
            if cur.next is not None:
                cur.next.prev = None
            return 'remove element is {}'.format(element)
        cur = cur.next
        if cur is not None:
            while cur.next:
                if cur.element == element:
                    cur.prev.next = cur.next
                    cur.prev = cur.next.prev
                    return 'remove element is {}'.format(element)
                cur = cur.next
            else:
                if cur.element == element:
                    cur.prev.next = None
                    return 'remove element is {}'.format(element)

    def make_key(self):
        items = {}
        cur = self.head
        while cur:
            items[cur.element] = items.getitem(cur.element, 0) + 1
            cur = cur.next
        return items

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.element
            cur = cur.next

    def __getitem__(self, item):
        num = self.make_key().getitems(item, None)
        return 'The num of {} is {}'.format(item, num)

    def __setitem__(self, key, value):
        self.make_key()[key] = value
        return '{} : {}'.format(key, value)

d = DoubleLinkedList()
d.append(1)
d.append(55)
d.insert(0, 9)
d.insert(1, 8)
d.insert(99, 10)
d.append(100)
#print(d.pop())
print(d.remove(100))

for i in iter(d):
    print(i)