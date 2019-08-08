from operator import mul
from functools import reduce, partial
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        numerator = min(m - 1, n - 1)
        denominator = m + n - 2
        if numerator == 0:
            return 1
        else:
            d, n  = map(partial(reduce, mul), zip(*zip(range(denominator, 0, -1), range(numerator, 0 , -1))))
            return d // n
