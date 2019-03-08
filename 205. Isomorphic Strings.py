class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        to = {}
        for i, j in zip(s, t):
            if i not in to:
                to[i] = j
            elif to[i] != j:
                return False
        if len(set(to.keys())) == len(set(to.values())):
            return True
        else:
            return False
