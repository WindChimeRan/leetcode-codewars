import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        times = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, times + 1))
