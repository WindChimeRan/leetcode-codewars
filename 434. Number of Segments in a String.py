# 1
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        
# 2
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '':
            return 0
        
        flag = True
        cnt = 1
        for i in range(len(s)):
            if s[i] == ' ':
                if flag == True:
                    cnt += 1
                    flag = False
            else:
                flag = True
        return cnt

# 3
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 0
        cnt = 0
        
        for i in s:
            if i != ' ':
                flag = 1
            else:
                cnt += flag
                flag = 0
        cnt += flag
        return cnt
                
                    
                
