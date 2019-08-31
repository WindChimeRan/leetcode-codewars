"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {}
        for e in employees:
                dic[e.id] = e
        imp = dic[id].importance
        
        sub = dic[id].subordinates
        while len(sub) > 0:
                new_sub = []
                for s in sub:
                        imp += dic[s].importance
                        new_sub.extend(dic[s].subordinates)
                sub = new_sub
        return imp
