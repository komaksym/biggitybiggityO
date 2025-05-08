# Time:  O(1)

# math
class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        return int(((1+8*len(grades))**0.5-1)/2.0)
