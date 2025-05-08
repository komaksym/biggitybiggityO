# Time:  O(nlogn)

import bisect


# binary search, longest increasing subsequence, lis
class Solution(object):
    def minOperations(self, nums):
        def longest_non_increasing_subsequence(arr):
            result = []
            for x in arr:
                right = bisect.bisect_right(result, -x)
                if right == len(result):
                    result.append(-x)
                else:
                    result[right] = -x
            return len(result)
        
        return longest_non_increasing_subsequence(nums)
