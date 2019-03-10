# 1
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit = []
        alpha = []
        alpha_dict = {}
        for log in logs:
            c = log.split()
            if c[1].isnumeric():
                digit.append(log)
            else:
                alpha_dict[log] = ' '.join(c[1:])
                alpha.append(log)
        alpha.sort(key=lambda x: alpha_dict[x])
        alpha.extend(digit)
        return alpha
        
# 2
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit = []
        alpha = []
        alpha_dict = {}
        for log in logs:
            c = log.split(' ', 1)
            if c[1][0].isnumeric():
                digit.append(log)
            else:
                alpha_dict[log] = c[1]
                alpha.append(log)
        alpha.sort(key=lambda x: alpha_dict[x])
        alpha.extend(digit)
        return alpha
