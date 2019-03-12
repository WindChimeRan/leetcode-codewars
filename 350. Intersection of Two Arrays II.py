class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        lazy = 0
        result = []
        for i in nums1:
            if i in nums2[lazy:]:
                lazy = nums2[lazy:].index(i) + 1 + lazy
                result.append(i)
                if lazy >= len(nums2):
                    break
        return result
