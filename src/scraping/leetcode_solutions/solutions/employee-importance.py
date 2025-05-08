# Time:  O(n)

import collections


"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if employees[id-1] is None:
            return 0
        result = employees[id-1].importance
        for id in employees[id-1].subordinates:
            result += self.getImportance(employees, id)
        return result


# Time:  O(n)
class Solution2(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        result, q = 0, collections.deque([id])
        while q:
            curr = q.popleft()
            employee = employees[curr-1]
            result += employee.importance
            for id in employee.subordinates:
                q.append(id)
        return result

