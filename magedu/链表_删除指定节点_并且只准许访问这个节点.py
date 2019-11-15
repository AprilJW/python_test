# 删除指定节点，并且只能访问这个节点
# 如果给定的节点是最后一个节点怎么办？

from LinkedList import ll

def remove(node):
    print('node:', node)
    if node.next:
        node.data = node.next.data
        node.next = node.next.next
    else:
        node.data = None

for i in ll:
    print(i)
print('*********')

remove(ll.head.next.next)

for i in ll:
    print(i)