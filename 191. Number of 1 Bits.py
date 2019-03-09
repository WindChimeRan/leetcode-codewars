# 1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
# 2
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            cnt += n % 2
            n //= 2
        return cnt
