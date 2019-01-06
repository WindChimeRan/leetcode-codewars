class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        self.flag = False
        tra_set = set()
        def tra(root, k):
            if root != None:
                if root.val not in tra_set:
                    tra_set.add(k - root.val)
                else:
                    self.flag = True
            else:
                return
            tra(root.left, k)
            tra(root.right, k)
            
        tra(root, k)
        return self.flag
                    
                
        
        
            
        
