# Time:  O(nlogn)

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        result = 1
        for i in range(1, len(arr)):
            result = min(result+1, arr[i])
        return result
