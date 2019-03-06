# 1

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        saved_row = set()
        saved_col = set()
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if c == 0:
                    saved_row.add(i)
                    saved_col.add(j)
        
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if i in saved_row or j in saved_col:
                    matrix[i][j] = 0
                    
                    
            
# 2

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        saved_col = set()
        saved_row = -1
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if c == 0:
                    saved_row = i
                    saved_col.add(j)
                    for t in range(i):
                        matrix[t][j] = 0
                if j in saved_col:
                    matrix[i][j] = 0
            if saved_row != -1:
                matrix[saved_row] = [0 for _ in r]
                saved_row = -1

# 3 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        saved_row = set()
        saved_col = set()
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if c == 0:
                    saved_row.add(i)
                    saved_col.add(j)
        
        for i in saved_row:
            matrix[i] = [0 for _ in range(len(matrix[0]))]
            
        for j in saved_col:
            for i in range(len(matrix)):
                matrix[i][j] = 0
            
        
