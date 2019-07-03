# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import functools
class Solution(object):
    
    @functools.lru_cache(maxsize=100)
    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
