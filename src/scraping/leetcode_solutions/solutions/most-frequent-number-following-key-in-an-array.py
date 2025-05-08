# Time:  O(n)

import collections


# freq table
class Solution(object):
    def mostFrequent(self, nums, key):
        return collections.Counter(nums[i+1] for i in range(len(nums)-1) if nums[i] == key).most_common(1)[0][0]
