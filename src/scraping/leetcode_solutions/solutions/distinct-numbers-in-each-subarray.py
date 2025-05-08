# Time:  O(n)

import collections


class Solution(object):
    def distinctNumbers(self, nums, k):
        result = []
        count = collections.Counter()
        for i, num in enumerate(nums):
            count[num] += 1
            if i >= k:
                count[nums[i-k]] -= 1
                if not count[nums[i-k]]:
                    del count[nums[i-k]]
            if i+1 >= k:
                result.append(len(count))
        return result

