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



l = LinkedList()
l.append(1).append(2).append(3).append(4).append(5).append(6)

for i in l:
    print(i)

print(len(l))


# 删除倒数第n个元素
# 要求不使用size
# 思路：第一个人先跑n步，第二个人再开始跑，当第二个人到达终点时，即为所求
# n=4向前走3步，n=2向前走1步
def remove(l, n):
    assert 0 < n <= len(l)

    fast = l.head
    while n > 1:  # 先向前走几步n > 0向前走n步
        fast = fast.next
        n -= 1

    slow = l.head
    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow

print(remove(l, 4))




