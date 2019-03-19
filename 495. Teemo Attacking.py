# 1
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if len(timeSeries) <= 1:
            return len(timeSeries) * duration
        
        poison = 0
        for cur, pre in zip(timeSeries[1:], timeSeries):
            poison += min(cur - pre, duration)
        return poison + duration
# 2
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if len(timeSeries) <= 1:
            return len(timeSeries) * duration
            
        return duration + sum(min(cur - pre, duration) 
                            for cur, pre in zip(timeSeries[1:], timeSeries))

