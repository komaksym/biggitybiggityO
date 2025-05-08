# Time:  O(nlogn)

from sortedcontainers import SortedList


# sorted list, binary search
class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        result = float("inf")
        sl = SortedList()
        for i in range(x, len(nums)):
            sl.add(nums[i-x])
            j = sl.bisect_left(nums[i])
            if j-1 >= 0:
                result = min(result, nums[i]-sl[j-1])
            if j < len(sl):
                result = min(result, sl[j]-nums[i])
        return result
