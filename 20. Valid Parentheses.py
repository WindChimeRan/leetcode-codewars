class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(':')', '[':']','{':'}'}
        stack = []
        for c in s:
            if c in left.keys():
                stack.append(c)
            else:
                if len(stack) > 0:
                    if left[stack.pop()] == c:
                        continue
                    else:
                        return False
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
