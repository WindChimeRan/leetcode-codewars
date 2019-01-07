# 1
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        
        if len(grid) == 1:
            return Node(val=grid[0][0], 
                        isLeaf=True, 
                        topLeft=None, 
                        topRight=None, 
                        bottomLeft=None, 
                        bottomRight=None
                       )
        
        glen = len(grid) // 2
        topLeft = [row[:glen] for row in grid[:glen]]
        topRight = [row[glen:] for row in grid[:glen]]
        bottomRight = [row[glen:] for row in grid[glen:]]
        bottomLeft = [row[:glen] for row in grid[glen:]]
        
        reduce_sum = lambda xss: sum(map(sum, xss))
        
        sumTopLeft, sumTopRight, sumBottomLeft, sumBottomRight = map(reduce_sum, (topLeft, topRight, bottomLeft, bottomRight))
        
        total = sumTopLeft + sumTopRight + sumBottomLeft + sumBottomRight
        
        if total == 0:
            root = Node(val=False, 
                        isLeaf=True, 
                        topLeft=None, 
                        topRight=None, 
                        bottomLeft=None, 
                        bottomRight=None
                       )
        elif total == glen * glen * 4:
            root = Node(val=True, 
                        isLeaf=True, 
                        topLeft=None, 
                        topRight=None, 
                        bottomLeft=None, 
                        bottomRight=None
                       )
        else:
            root = Node(val=False, 
                        isLeaf=False, 
                        topLeft=self.construct(topLeft), 
                        topRight=self.construct(topRight), 
                        bottomLeft=self.construct(bottomLeft), 
                        bottomRight=self.construct(bottomRight)
                       )
        return root
        
                                                                     
