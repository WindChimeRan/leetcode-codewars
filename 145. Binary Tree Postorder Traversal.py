# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            else:
                postorder(root.left)
                postorder(root.right)
                r.append(root.val)
                
        r = []
        postorder(root)

        return r
