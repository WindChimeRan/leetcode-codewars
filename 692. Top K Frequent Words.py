from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words).most_common()
        res = sorted(cnt, key=lambda x: (-x[1], x[0]))
        return [w for w, v in res[:k]]
