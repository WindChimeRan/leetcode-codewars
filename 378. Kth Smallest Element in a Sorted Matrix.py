from functools import reduce
from operator import add
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(reduce(add, matrix), reverse=False)[k-1]
