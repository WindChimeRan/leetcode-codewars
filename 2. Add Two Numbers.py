# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def rec(l1, l2, forward):
                if l1 and l2:
                        cur = ListNode((l1.val + l2.val + forward) % 10)
                        forward = (l1.val + l2.val + forward) // 10
                elif l1:
                        cur = ListNode((l1.val + forward) % 10)
                        forward = (l1.val + forward) // 10
                elif l2:
                        cur = ListNode((l2.val + forward) % 10)
                        forward = (l2.val + forward) // 10
                else:
                        if forward > 0:
                                cur = ListNode(forward)
                        else:
                                cur = None
                        forward = 0
                return cur, forward
        forward = 0
        begin, _ = cur, forward = rec(l1, l2, forward)
        while cur:
                if l1:
                        l1 = l1.next
                if l2:
                        l2 = l2.next
                cur.next, forward = rec(l1, l2, forward)
                cur = cur.next
        return begin
