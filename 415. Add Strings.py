# 1
from itertools import zip_longest
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        result = []
        for a, b in zip_longest(reversed(num1), reversed(num2)):
            a = '0' if a is None else a
            b = '0' if b is None else b
            num = int(a) + int(b) + carry
            carry = num // 10
            r = num % 10
            result.append(r)
        if carry!= 0:
            result.append(carry)
        return ''.join(map(str, reversed(result)))
