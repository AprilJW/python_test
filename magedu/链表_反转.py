from LinkedList import ll as ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur.next:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt

        return cur
s = Solution()
cur = s.reverseList(ListNode.head.next)
while cur:
    print(cur.data)
    cur = cur.next



# # 判断是否有环
# # 方法1：双指针
# # 方法2：在Node类上增加一个visited属性，打标记
# # 方法3：放到set中
#
# def has_cycle(ll):
#     if ll.head is None or ll.head.next is None:
#         return False
#
#     fast = ll.head
#     slow = ll.head
#     while fast is not None and fast.next is not None:
#         fast = fast.next.next
#         slow = slow.next
#         if fast == slow:
#             return True
#     return False
#
# # print(has_cycle(ll))
# k = 0
# # for node in ll:
# #     print(node)
# #
# for i, node in enumerate(ll):
#     if k >= 2:
#         break
#     k += 1
# print('in:', node)
# ll.tail.next = node
#
# # print('+++++++++')
# # for node in ll:
# #     print(node)
# # print('+++++++++++')
# print(has_cycle(ll))
#
# # 找到环的开始节点
# # 快慢指针，相遇节点到环入口的距离等于head指针到环入口的距离，距离设为k
# # 推理：当慢指针刚好走到环入口时，快慢指针的距离为k等于head到环入口的距离k
# # 当快慢指针在环内部相遇时，两个指针一起出发快的指针到达原来的位置，慢的的指针
# # 也到达原来的位置，慢指针向后退x步，快指针向后退2x步，2x-x = k, 所以相遇点到
# # 环入口的距离也为k, 当指针在环内相遇时，将一个指针移动到head，另一个指针还是留在
# # 相遇点，现在2个指针同时以一步步长，向前走，当再次相遇时即为环入口。
#
# def find_start(ll):
#     assert has_cycle(ll)
#     print('*******')
#     fast = ll.head
#     slow = ll.head
#
#     while fast is not None and fast.next is not None:
#         fast = fast.next.next
#         slow = slow.next
#         if fast == slow:
#             print('===:', fast, slow)
#             fast = ll.head
#             break
#
#     while fast != slow:
#         fast = fast.next
#         slow = slow.next
#         print('one step:', fast, slow)
#     return slow
#
#
# innode = find_start(ll)
# print('环：', innode)




