# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def trav(root: TreeNode, r):
            if root == None:
                return root
            else:
                trav(root.left, r)
                r.append(root.val)
                trav(root.right, r)
        
        result = []
        trav(root, result)
        
        root = temp = TreeNode(result[0])
        
        if len(result) == 1:
            return root
        else:
            for i in range(1, len(result)):
                temp.right = TreeNode(result[i])
                temp = temp.right
            return root
