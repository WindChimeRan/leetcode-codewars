# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from itertools import chain
class Solution(object):
    

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        def generator(head):
            while head:
                yield head
                head = head.next
            
        for a, b in zip(chain(generator(headA), generator(headB)), chain(generator(headB), generator(headA))):
            if a is b:
                return a
        else:
            return None
            
