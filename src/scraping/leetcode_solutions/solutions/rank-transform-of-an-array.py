# Time:  O(nlogn)

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return list(map({x: i+1 for i, x in enumerate(sorted(set(arr)))}.get, arr))
