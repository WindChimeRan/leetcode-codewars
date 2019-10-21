# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
                if len(nums) == 0:
                        return None
                pos = 0
                max_num = nums[0]
                for i, n in enumerate(nums):
                        if n > max_num:
                                max_num = n
                                pos = i
                root = TreeNode(max_num)
                root.left = self.constructMaximumBinaryTree(nums[:pos])
                root.right = self.constructMaximumBinaryTree(nums[pos+1:])
                return root
