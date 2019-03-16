class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        import sys
        
        r = -sys.maxsize
        
        if k == 1:
            return max(nums)
        
        cur = sum(nums[:k])
        r = cur
        for i in range(1, len(nums) - k + 1):
            cur = cur - nums[i-1] + nums[i + k - 1]
            r = max(cur, r)
            
        return r / k
            
