# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def dfs(root, sum):
            count = 0
            if not root:
                return 0
            if root.val == sum:
                count += 1
            else:
                count += dfs(root.left, sum - root.val)
                count += dfs(root.right, sum - root.val)
            return count
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
