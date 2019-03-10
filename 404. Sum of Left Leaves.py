# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        cnt = 0
        def inorder(root: TreeNode, state: bool):
            nonlocal cnt
            if not root:
                return
            else:
                inorder(root.left, state=True)
                if not root.left and not root.right and state:
                    cnt += root.val
                inorder(root.right,state=False)
        
        inorder(root, False)
        return cnt
