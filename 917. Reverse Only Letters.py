class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = list(filter(lambda x:x.isalpha(), (S)))
        return ''.join(stack.pop() if s.isalpha() else s for s in S)
