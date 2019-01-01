# 0 best
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 1
            else:
                return i
# 1
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) // 2
        cnt = dict()
        for a in A:
            cnt.setdefault(a, 0)
            cnt[a] += 1
        for k in cnt:
            if cnt[k] == n:
                return k


# 2
from collections import Counter
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt = Counter(A)
        return cnt.most_common(1)[0][0]

# 3 bad
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sa = A.sort()
        cnt = 1
        pre = A[0]
        for i in range(1, len(A)):
            cur = A[i]
            if cur == pre:
                cnt += 1
            else:
                pre = cur
                cnt = 1
            if cnt == len(A) // 2:
                return pre
            
