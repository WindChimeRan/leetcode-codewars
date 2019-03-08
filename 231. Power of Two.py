# 1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in (pow(2, i) for i in range(32))

# 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            return n & (n - 1) == 0
