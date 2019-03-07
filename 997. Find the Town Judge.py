# 1
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l = {i:[] for i in range(1,N+1)}
        r = {i:[] for i in range(1,N+1)}
        
        for a, b in trust:
            r[b].append(a)
            l[a].append(b)
        for i in range(1, N+1):
            if len(l[i]) == 0 and len(r[i]) == N - 1:
                return i
        return -1
