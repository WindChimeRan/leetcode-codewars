from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        paths_d = defaultdict(list)
        for i, o in paths:
            paths_d[i].append(o)
            paths_d[o].append(i)
        result_l = []
        result_d = {}
        a = {1, 2, 3, 4}
        for i in range(1, N + 1):
            if i not in paths_d:
                cur = 1
            else:
                cur = (a - {result_d.get(p, 0) for p in paths_d[i]}).pop()
            result_l.append(cur)
            result_d[i] = cur
        return result_l
                
