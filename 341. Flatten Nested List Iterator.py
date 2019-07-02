# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def gene(nestedList):
            for elem in nestedList:
                if elem.isInteger():
                    yield elem.getInteger()
                else:
                    for ne in gene(elem.getList()):
                        yield ne
                    
        self.generator = gene(nestedList)
        self.flag = True
        self.to_append = None

        
    def next(self):
        """
        :rtype: int
        """
        return self.to_append
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.to_append = next(self.generator)
        except:
            self.flag = False
            self.to_append = None
        return self.flag
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
