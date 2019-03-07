# 1
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        left = right = 0
        for num, i in enumerate(s):
            if i == '(':
                stack.append(i)
            if i == '*':
                left += 1
                right += 1
            if i == ')':
                if len(stack) > 0:
                    stack.pop()
                    if len(stack) == 0:
                        right = 0
                    if len(stack) < right:
                        right = len(stack)
                elif left > 0:
                    left -= 1
                    right = 0
                else:
                    return False
        
        if len(stack) <= right:
            return True
        else:
            return False
                
