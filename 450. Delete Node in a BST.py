# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_min(self, root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif root.val == key and (not root.left) and (not root.right):
            return None
        elif root.val == key and not root.left:
            return root.right
        elif root.val == key and not root.right:
            return root.left
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val == key:
            # some magic
            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        else:
            print('error')
        return root
            

            
        
