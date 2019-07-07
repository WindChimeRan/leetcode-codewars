from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s).most_common()
        res = []
        for k, t in cnt:
            res.append(k*t)
        return ''.join(res)
