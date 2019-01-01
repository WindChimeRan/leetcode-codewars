class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = lambda x: x%2 == 1
        even = lambda x: not odd(x)
        
        result = []
        for o, e in zip(filter(odd, A), filter(even, A)):
            result.extend([e, o])
        return result
        
        