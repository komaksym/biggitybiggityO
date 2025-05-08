# Time:  O(n)

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        return sum(max((target[i] if i < len(target) else 0)-(target[i-1] if i-1 >= 0 else 0), 0) for i in range(len(target)+1))
