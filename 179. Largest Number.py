from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        result = sorted(nums, key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        if result[0] == '0':
                return '0'
        else:
                return ''.join(result)
        
