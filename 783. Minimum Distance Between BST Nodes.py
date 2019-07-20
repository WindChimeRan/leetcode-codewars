# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        min_diff = float('inf')
        last = None
        def bst(root):
            nonlocal last, min_diff
            
            if not root:
                return
            bst(root.right)
            if last:
                min_diff = min(min_diff, abs(last-root.val))
            last = root.val
            bst(root.left)
        
        bst(root)
        
        return min_diff
