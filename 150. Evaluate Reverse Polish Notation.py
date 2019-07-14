class Solution:
    def eval_op(self, op, a1, a2):
        
        if op == '+':
            return a1 + a2
        elif op == '-':
            return a1 - a2
        elif op == '*':
            return a1 * a2
        elif op == '/':
            return abs(a1) // abs(a2) * (1 if a1 * a2 > 0 else -1)
        else:
            print('error')
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(self.eval_op(t, a2, a1))
            else:
                stack.append(int(t))
        return stack.pop()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t = tokens.pop()
        if t in '+-*/':
            a = self.evalRPN(tokens)
            b = self.evalRPN(tokens)
            t = eval(str(b) + t + str(a))
        return int(t)
