# 1
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for i, s in enumerate(S.split(), 1):
            if s[0] in 'aeiouAEIOU':
                s = s + 'ma'
            else:
                s = s[1:] + s[0] + 'ma'
            s = s + i * 'a'
            result.append(s)
        return ' '.join(result)

