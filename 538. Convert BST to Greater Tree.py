# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        inc_sum = 0
        def rev_bst(root):
            nonlocal inc_sum
            if not root: return
            rev_bst(root.right)
            root.val += inc_sum
            inc_sum = root.val
            rev_bst(root.left)
        
        rev_bst(root)
        return root
