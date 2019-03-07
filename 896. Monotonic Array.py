# 1
from functools import partial
from operator import eq, ne, le, lt
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        else:
            return le(len(set(map(partial(lt, 0), filter(partial(ne, 0), (i - j for i, j in zip(A, A[1:])))))), 1)

# 2
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        else:
            inc = True
            dec = True
            
            for i in range(1, len(A)):
                residual = A[i] - A[i-1]
                inc &= residual >= 0
                dec &= residual <= 0
            return inc or dec
                
                
            
            
            
