# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def complete(r):
            if not r:
                return ''
            elif not r.left and not r.right:
                return str(r.val)
            else:
                return str(r.val) + ('(' + complete(r.left) + ')' )+  ('' if not r.right else '(' + complete(r.right) + ')')
        result = complete(t)
        return result
