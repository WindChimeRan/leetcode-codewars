# 1
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        do = ndo = 0
        for n in nums:
            do, ndo = max(ndo, do), do + n
        return max(do, ndo)
