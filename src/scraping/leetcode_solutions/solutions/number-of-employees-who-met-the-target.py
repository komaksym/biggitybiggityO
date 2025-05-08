# Time:  O(n)

# array
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        
        return sum(x >= target for x in hours)
