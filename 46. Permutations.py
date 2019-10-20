# 1
from functools import partial
from operator import add

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            temp = nums[:]
            
            fst = temp.pop(i)
            one = list(map(partial(add, [fst]), self.permute(temp)))
            result.extend(one)
            
        return result
            
            
# 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
                return [nums]
        else:
                out = []
                for i in range(len(nums)):
                        fst = [nums[i]]
                        res = nums[:i] + nums[i+1:]
                        for part in self.permute(res):
                                out.append(fst+part)
                return out
