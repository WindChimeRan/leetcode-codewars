# 1
from collections import Counter
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        ab = []
        for i in points:
            aib = []
            for j in points:
              aib.append(dist(i, j))
            ab.append(aib)
        cnt = 0
        for i in ab:
            counter_ab = Counter(i)
            for k in counter_ab:
                if k != 0:
                    cnt += counter_ab[k] * (counter_ab[k]-1)
        return cnt
# 2
from collections import Counter
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dist = lambda x, y: x * x + y * y
        cnt = 0
        for i in points:
            counter_ab = Counter(dist(i[0]-j[0], i[1]-j[1]) for j in points)
            cnt += sum(counter_ab[k] * (counter_ab[k]-1) for k in counter_ab if k != 0)

        return cnt
