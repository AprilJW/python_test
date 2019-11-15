from LinkedList import ll
# 将一个链表分半，生成2个新链表
# 一个指针走2步，一个指针走一步，奇数刚好，偶数停在倒数第二个

def split(ll):
    head = ll.head
    if head is None:
        return
    fast = head
    slow = head
    while fast and fast.next:
        # fast非空可以取到fast.next，fast.next非空可以取到fast.next.next
        # 当中间是and时fast在前fast.next在后，因为如果发生短路，则到第一个条件就停止
        # 第二个条件不会被取到
        fast = fast.next.next
        slow = slow.next
    cur = slow
    head2 = None
    head2 = cur.next
    cur.next = None
    return ll

# for i in split(ll):
#     print(i)

# 找到中间节点单向列表不使用(size）
# 方法1：对于偶数个节点，返回中间偏右，对于奇数个节点返回中间
# 方法2：见代码split，对于偶数个节点，返回中间偏左，对于奇数个节点返回中间
def find(ll):
    if ll is None:
        return
    fast = ll.head
    slow = ll.head
    while True:
        if fast.next is None:
            return slow
        if fast.next is not None and fast.next.next is None:
            return slow.next
        fast = fast.next.next
        slow = slow.next


print(find(ll))


# 找到中间节点双向列表（不使用size）
# n1.next n2.prev,当两个指针重叠，或者相互穿过时即为中间节点