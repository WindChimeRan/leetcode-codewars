class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        def check(x):
            if -2**31 <= x <= 2**31-1:
                return x
            else:
                return 0
            
        return check(sign * (int(''.join(reversed(str(abs(x)))))))
