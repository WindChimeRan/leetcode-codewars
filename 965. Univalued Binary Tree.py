# 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left and root.right:
            if root.val == root.left.val == root.right.val:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            else:
                return False
        elif root.left:
            if root.val == root.left.val:
                return self.isUnivalTree(root.left)
            else:
                return False
        elif root.right:
            if root.val == root.right.val:
                return self.isUnivalTree(root.right)
            else:
                return False
        else:
            return True
