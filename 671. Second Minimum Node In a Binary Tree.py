# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min1, min2 = float('inf'), float('inf')
        def add_node(val):
            nonlocal min1, min2
            if val < min1:
                min1, min2 = val, min1
            elif min1 < val < min2:
                min2 = val
                
                
        def bst(root):
            if not root:
                return 
            bst(root.left)
            add_node(root.val)
            bst(root.right)
        
        bst(root)
        
        if min2 == float('inf'):
            return -1
        else:
            return min2
                
