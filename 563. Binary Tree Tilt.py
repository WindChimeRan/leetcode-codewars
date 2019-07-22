# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        @lru_cache(10)
        def sumTree(root):
            if not root:
                return 0
            else:
                return sumTree(root.left) + root.val + sumTree(root.right)
            
        if not root:
            return 0
        else:
            return abs(sumTree(root.left) - sumTree(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
        
