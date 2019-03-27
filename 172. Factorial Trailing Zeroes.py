class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = n - n % 5
        cnt = five // 5
        two = 2
        init = 100
        ten = n
        while ten // pow(5, two) != 0:
            cnt += ten // pow(5, two)
            init *= 10
            two += 1
        return cnt
