# 1
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        end = rt = int(sqrt(c))
        for i in range(rt + 1):
            for j in range(end, i - 1, -1):
                if i**2 + j**2 == c:
                    return True
                elif i**2 + j**2 < c:
                    break
                else:
                    end -= 1
        return False
