class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = []
        for char in zip(*strs):
            if len(set(char)) == 1:
                result.append(char[0])
            else:
                break
        return ''.join(result)