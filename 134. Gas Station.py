# 就是首先要找到可以让剩余油量大于0的加油站，然后假设这个加油站是起点继续往后走，
# 如果能走到尽头（还有油量剩余）那么这时的剩余油量大于该点之前的所需油量就可以走完，如果走着走着发现油不够了，就从下一个加油站开始走
#
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
        
