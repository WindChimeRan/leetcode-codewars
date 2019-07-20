# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        def tolist(root):
            if not root:
                return []
            else:
                return tolist(root.left) + [root.val] + tolist(root.right)
            
        return tolist(root)[k-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        def tolist(root):
            if not root:
                return
            else:
                yield from tolist(root.left)
                yield root.val
                yield from tolist(root.right)
            
        for i, v in enumerate(tolist(root)):
            if i == k-1:
                return v
