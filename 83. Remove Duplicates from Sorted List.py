# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        def recur(head):
            
            if not head or not head.next:
                return
            if head.val == head.next.val:
                head.next = head.next.next
                recur(head)
            else:
                recur(head.next)
        recur(head)
        return head
