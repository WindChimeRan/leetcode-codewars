from collections import Counter
from functools import reduce

import operator

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return list(reduce(operator.and_, map(Counter, A)).elements())
        
