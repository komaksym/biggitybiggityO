# Time:  O(n^2)

import collections


# freq table
class Solution(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j])%d in cnt:
                    result += cnt[(nums[i]+nums[j])%d]
            cnt[-nums[i]%d] += 1
        return result


# Time:  O(n^2)
import collections


# freq table
class Solution2(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for i in range(len(nums)):
            if nums[i]%d in cnt:
                result += cnt[nums[i]%d]
            for j in range(i):
                cnt[-(nums[i]+nums[j])%d] += 1
        return result


# Time:  O(n^2)
import collections


# freq table
class Solution3(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            cnt = collections.Counter()
            for j in range(i+1, len(nums)):
                result += cnt[nums[j]%d]
                cnt[-(nums[i]+nums[j])%d] += 1
        return result
