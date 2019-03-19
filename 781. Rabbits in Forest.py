from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers) == 0:
            return 0
        
        cnt = Counter(answers)
        r = 0
        
        for k, v in cnt.items():
            if k == 0:
                r += v
            elif k + 1 >= v:
                r += k + 1
            else:
                r += (v // (k + 1)) * (k + 1)
                r += 0 if v % (k + 1) == 0 else k + 1
        return r
