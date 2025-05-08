# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1]-x[0]) 
        result = 0
        for a, m in tasks: 
            result = max(result+a, m)
        return result


# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[0]-x[1]) 
        result = curr = 0
        for a, m in tasks: 
            result += max(m-curr, 0)
            curr = max(curr, m)-a
        return result
