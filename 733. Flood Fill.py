class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        def isValid(x, y):
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
                return False
            else:
                return True
        
        def operate(x, y):
            if (x, y) not in result and isValid(x, y) and image[x][y] == ocolor:
                stack.append((x, y))
                result.add((x, y))
        
        ocolor = image[sr][sc]
        
        stack = [(sr, sc)]
        result = set()
        result.add((sr, sc))
        
        while stack != []:
            cx, cy = stack.pop()
            operate(cx - 1, cy)
            operate(cx + 1, cy)
            operate(cx, cy - 1)
            operate(cx, cy + 1)
        
        while len(result) != 0:
            x, y = result.pop()
            image[x][y] = newColor
            
        return image
            
        
        
        
        
