class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        diff = (g - c for g, c in zip(gas, cost))

        tank = total = 0
        pos = 0
        for i, cur in enumerate(diff):
            tank += cur
            if tank < 0:
                total += tank
                tank = 0
                pos = i + 1
        return pos if total + tank >= 0 else -1
        
