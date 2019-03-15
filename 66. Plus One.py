# 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        num = list(map(int, str(num)))
        return num
# 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            cur = digits[i] + carry
            carry = cur // 10
            digits[i] = cur % 10
            if cur < 10:
                return digits
            else:
                carry = 1
                digits[i] %= 10
        if carry > 0:
            digits = [1] + digits
            return digits
