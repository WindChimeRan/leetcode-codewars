from operator import sub, add
from functools import partial

class Solution:
    def calculate(self, s: str) -> int:
        
        symbol = ['(', ')', '+', '-']
        
        def tokenizer(s):
            s = s.replace(' ', '')
            for sym in symbol:
                s = s.replace(sym, ' ' + sym + ' ')
            tokens = ['('] + s.split() + [')']
            return tokens
        
        tokens = tokenizer(s)
        
        stack = []
        
        for t in tokens:
            if t == '(':
                stack.append('(')
            elif t in ('+', '-'):
                stack.append(t)
            elif t == ')':
                res = None
                eval_stack = []

                while True:
                    n = stack.pop()
                    op = stack.pop()
                    
                    if op == '(':
                        res = n
                        for f in reversed(eval_stack):
                            res = f(res)
                        stack.append(res)
                        break
                    elif op == '+':
                        eval_stack.append(partial(add, n))
                    elif op == '-':
                        eval_stack.append(partial(add, -n))
                    else:
                        print('error')
                        
            else:
                num = int(t)
                stack.append(num)
            
        return stack[-1]
                
                
            
