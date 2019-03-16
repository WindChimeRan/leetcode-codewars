# 1
import sys

from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_cnt = cnt.most_common(1)[0][1]
        
        end = [k for k, v in cnt.items() if v == max_cnt]

        result = sys.maxsize
        
        for tok in end:
            left = nums.index(tok)
            right = len(nums) - 1 - list(reversed(nums)).index(tok)
            result = min(result, right-left+1)
        return result
        
# 2
import sys

from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_cnt = cnt.most_common(1)[0][1]
        
        if max_cnt == 1:
            return 1
        
        end = [k for k, v in cnt.items() if v == max_cnt]

        result = sys.maxsize
        
        for tok in end:
            left = nums.index(tok)
            
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == tok:
                    right = i
                    break
            result = min(result, right-left+1)
        return result
        
