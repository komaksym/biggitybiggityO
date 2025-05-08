# Time:  O(nlogn + qlogn)

import bisect


# greedy, sort, binary search
class Solution(object):
    def answerQueries(self, nums, queries):
        
        nums.sort()
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        return [bisect.bisect_right(nums, q) for q in queries]
