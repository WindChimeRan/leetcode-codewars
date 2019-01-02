class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        result = []
        max_n = len(S)
        min_n = 0
        
        for s in S:
            if s == 'I':
                result.append(min_n)
                min_n += 1
            else:
                result.append(max_n)
                max_n -= 1
        result.append(min_n)
        return result