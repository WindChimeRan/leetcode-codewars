# 1
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort(key=lambda x: -x)
        
        @lru_cache(10000)
        def helper(amount: int) -> int:
            if amount == 0:
                return 0
            elif amount in coins:
                return 1
            elif amount < min(coins):
                return 1000000
            return 1 + min(helper(amount - i) for i in coins)
        
        r = helper(amount) 
        return -1 if r>= 1000000 else r
# 2
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import sys
        
        memo = [sys.maxsize for i in range(amount+1)]
        
        for idx in range(amount+1):
            if idx == 0:
                memo[idx] = 0
            else:
                minn = sys.maxsize
                for coin in coins:
                    if idx - coin >= 0:
                        minn = min(minn, 1 + memo[idx - coin])
                memo[idx] = minn
        r = memo[amount] 
        return r if r < sys.maxsize else -1
# 3 TODO
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        # 硬币总个数
        result = amount+1
        max_length = len(coins)-1
        
        def update(index,target,count):
            nonlocal result
            if count+math.ceil(target/coins[index])>=result:
                return
            
            if target%coins[index]==0:
                result = count + target//coins[index]
        
            if index==max_length:
                return
            
            # 从多到少依次尝试取出当前币值的硬币
            for coin_num in range(target//coins[index],-1,-1):
                update(index+1, target-coins[index]*coin_num, count+coin_num)
        update(0,amount,0)
        return -1 if result == amount+1 else result
        
