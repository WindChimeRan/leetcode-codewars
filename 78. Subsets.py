import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        for i in range(2 ** length):
            tmp = []
            for j in range(length):
                if (i >> j) % 2 == 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
