# Time:  O(nlogn)

from sortedcontainers import SortedList


# prefix sum, two pointers, sliding window, sorted list, binary search
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        INF = float("inf")
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        result = INF
        sl = SortedList()
        for i in range(len(nums)):
            if i-l+1 >= 0:
                sl.add(prefix[i-l+1])
            if i-r >= 0:
                sl.remove(prefix[i-r])
            idx = sl.bisect_left(prefix[i+1])-1
            if idx >= 0:
                result = min(result, prefix[i+1]-sl[idx])
        return result if result != INF else -1
