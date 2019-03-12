# 1
from itertools import zip_longest
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        def toTuples(s: str):
            if s == '':
                return []
            else:
                pre = None
                cnt = 0
                for i, cur in enumerate(s):
                    if not pre:
                        pre = cur
                        cnt += 1
                    elif pre != cur:
                        yield (pre, cnt)
                        pre = cur
                        cnt = 1
                    else:
                        cnt += 1
                yield (pre, cnt)
                
        for t, n in zip_longest(toTuples(typed), toTuples(name)):
            if not t or not n:
                return False
            if n[0] == t[0] and n[1] <= t[1]:
                continue
            else:
                return False
        else:
            return True
