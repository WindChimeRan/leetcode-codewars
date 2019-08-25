# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if fast is slow:
                break
        if fast and slow and fast is slow:
            # phrase 2 
            # begin from the meeting place
            ptr1 = head
            ptr2 = fast
            while ptr1 != ptr2:
                ptr1 = ptr1. next
                ptr2 = ptr2.next
            return ptr1
        else:
            return None
        
