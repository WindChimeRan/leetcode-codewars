# 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import functools
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def isa(root, q):
            if root == q:
                return True
            if root == None:
                return False
            if root.val > q.val:
                return isa(root.left, q)
            if root.val < q.val:
                return isa(root.right, q)

        if root == p or root == q:
            return root
        
        if p.val > q.val:
            p, q = q, p
            
        if root.left == p and root.right == q:
            return root
        
        if root.left and isa(root.left, p) and isa(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.right and isa(root.right, p) and isa(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)           
        return root
        
# 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root    
            
            
        