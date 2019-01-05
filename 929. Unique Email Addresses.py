# 1
from itertools import takewhile
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def norm(email):
            local, domain = email.split('@')
            local = filter(lambda c: c!= '.', takewhile(lambda c: c != '+', local))
            local = ''.join(local)
            return local + '@' + domain
        return len(set(map(norm, emails)))
            
# 2
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        e_set = set()
        for email in emails:
            local, domain = email.split('@')
            local = local[:local.find('+')].replace('.', '')
            e_set.add(local + '@' + domain)
        return len(e_set)
