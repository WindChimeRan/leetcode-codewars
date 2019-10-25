# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def swap(node, last, lastlast):
                if lastlast:
                        lastlast.next = node
                last.next = node.next
                node.next = last
                
                
        def f_0(node, last, lastlast):
                if node.next is None:
                        return
                else:
                        node, last, lastlast = node.next, node, last
                        f_1(node, last, lastlast)
                        
        def f_1(node, last, lastlast):
                swap(node, last, lastlast)
                if last.next is None:
                        return
                else:
                        node, last, lastlast = last.next, last, node
                        f_0(node, last, lastlast)
        
        if not head:
                return
        elif not head.next:
                return head
        else:
                result = head.next
                f_0(head, None,None)
                return result

        
