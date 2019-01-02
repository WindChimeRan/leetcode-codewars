# 1
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        ind = set()
        
        for t in range(len(A[0])):
            for i in range(1, len(A)):
                if A[i][t] < A[i-1][t]:
                    ind.add(t)
        return len(ind)
# 2
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        cnt = 0
        for chars in zip(*A):
            if list(chars) != sorted(chars):
               cnt += 1
        return cnt

            
                    