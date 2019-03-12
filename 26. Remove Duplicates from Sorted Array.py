# 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        else:
            pre = nums[-1]
            cnt = n
            for i in range(n-2, -1, -1):
                cur = nums[i]
                if cur == pre:
                    del nums[i+1]
                    cnt -= 1
                pre = cur

            return cnt
            
