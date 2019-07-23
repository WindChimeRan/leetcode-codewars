# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.cur = None
        self.ahead = None
        self.hasnext = False if not root else True
        self.gen = self.toGen(self.root)

    
    def toGen(self, root: TreeNode):
        if not root:
            return 
        else:
            yield from self.toGen(root.left)
            yield root.val
            yield from self.toGen(root.right)
            

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # self.cur =  next(self.gen) if not self.cur else self.ahead
        
        if self.cur is None:
            self.cur = next(self.gen)
        else:
            self.cur = self.ahead
            
        try:
            self.ahead = next(self.gen)
        except:
            self.hasnext = False
        return self.cur
        
    
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.hasnext
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
