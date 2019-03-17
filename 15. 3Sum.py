# 1
from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        cnt = Counter({k: min(3, v) for k, v in Counter(nums).items()})
        
        nums = sorted(cnt.elements())
        
        result = set()
        s = set(nums)
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                
                if -(a+b) in s:
                    for k in range(len(nums)-1, j, -1):
                        c = nums[k]
                        if a + b + c < 0:
                            break
                        if a + b + c == 0:
                            tri = tuple(([a, b, -(a + b)]))
                            result.add(tri)

        return list(result)
