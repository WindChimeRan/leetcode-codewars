import heapq
from operator import neg


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stack = sorted(stones, reverse=False)
        heap = list(map(neg, stones))
        heapq.heapify(heap)
        while True:
            
            if len(heap) == 0:
                return 0
            elif len(heap) == 1:
                return neg(heap[0])
            else:
                a = heapq.heappop(heap)
                b = heapq.heappop(heap)
                if a - b < 0:
                    heapq.heappush(heap, a - b)
            
