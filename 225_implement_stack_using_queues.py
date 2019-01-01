from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dq1 = deque()
        self.dq2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.dq1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        len1 = len(self.dq1)
        # t = self.dq1.popleft()
        for i in range(len1):
            t = self.dq1.popleft()
            if i == len1-1:
                self.dq1, self.dq2 = self.dq2, self.dq1
                return t
            self.dq2.append(t)
            
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        len1 = len(self.dq1)
        for i in range(len1):
            t = self.dq1.popleft()
            self.dq2.append(t)
            if i == len1 - 1:
                self.dq1, self.dq2 = self.dq2, self.dq1
                return t
            
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.dq1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()