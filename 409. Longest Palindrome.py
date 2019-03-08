class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            s = sorted(s)
            cnt = 1
            clist = []
            for i in range(1, len(s)):
                pre = s[i-1]
                cur = s[i]
                if pre != cur:
                    clist.append(cnt)
                    cnt = 1
                else:
                    cnt += 1
            clist.append(cnt)
            
            result = 0
            add_one = False
            for i in clist:
                if i % 2 == 0:
                    result += i
                else:
                    result += (i - 1 if i > 1 else 0)
                    add_one = True
            if add_one:
                result += 1
            return result
                    

            
            
