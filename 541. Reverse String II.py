class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        xs = list(s)
        flag = True
        for i in range(0, len(s), k):
            if flag:
                xs[i:i+k] = reversed(s[i:i+k])
            flag ^= True
        return ''.join(xs)
