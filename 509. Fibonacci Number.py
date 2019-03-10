# 1
from functools import lru_cache
class Solution:
    @lru_cache(2)
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)
# 2
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            pre = 0
            cur = 1
            for i in range(2, N + 1):
                pre, cur = cur, cur + pre
            return cur
            
