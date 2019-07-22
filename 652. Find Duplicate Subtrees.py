# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        saved = defaultdict(list)
        def pre(root):
            if not root:
                return 'None'
            else:
                s = '__'.join((str(root.val), pre(root.left), pre(root.right)))
                saved[s].append(root)
                return s
        pre(root)
        ans = [v[0] for v in saved.values() if len(v) > 1]
        return ans
