class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[target - n] = i 
            else:
                return [d[n], i]
        
