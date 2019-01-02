# 1
class RecentCounter:

    def __init__(self):
        self.pqueue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.pqueue.append(t)
        idx = 0
        for i in range(len(self.pqueue)):
            if self.pqueue[i]+3000-t<0:
                idx = i+1
            else:
                break
        self.pqueue = self.pqueue[idx:]
        return len(self.pqueue)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# 2
from collections import deque

class RecentCounter:

    def __init__(self):
        self.pqueue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        while self.pqueue and self.pqueue[0] + 3000 < t:
            self.pqueue.popleft()
        self.pqueue.append(t)
        return len(self.pqueue)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)