# 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_right_min(root):
            if root.left:
                return get_right_min(root.left)
            else:
                return root.val
        def get_left_most(root):
            if root.right:
                return get_left_most(root.right)
            else:
                return root.val
        cur = root.val
        left = cur - get_left_most(root.left) if root.left else None
        right = get_right_min(root.right) - cur if root.right else None
        releft = self.getMinimumDifference(root.left) if root.left else None
        reright = self.getMinimumDifference(root.right) if root.right else None
        result = list(filter(lambda x: x, (left, right, releft, reright)))
        return min(result) if result else None

# 2
class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lis = []
        def trav(root):
            if root.right:
                trav(root.right)
            lis.append(root.val)
            if root.left:
                trav(root.left)
        trav(root)
        return min(bigger-big for bigger, big in zip(lis, lis[1:]))
# 3
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = pre = residual = None
        
        def trav(root):
            nonlocal cur, pre, residual
            if root.right:
                trav(root.right)
            if cur:
                cur, pre = root.val, cur
                residual = min(residual, pre-cur) if residual else pre-cur
            else:
                cur = root.val
            if root.left:
                trav(root.left)
        trav(root)
        return residual
