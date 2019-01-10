# 1
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=5000)
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1: return len(word2)
        if not word2: return len(word1)
        return min(
            self.minDistance(word1[1:],word2[1:]) + int(not word1[0]==word2[0]),
            self.minDistance(word1, word2[1:]) + 1,
            self.minDistance(word1[1:], word2) + 1
        )
        
