# Time:  O(n)

import collections


class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        K = 2
        cnt = collections.Counter()
        for nums in nums1, nums2, nums3:
            cnt.update(set(nums))
        return [x for x, c in cnt.items() if c >= K]


# Time:  O(n)
import collections


class Solution2(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        K = 2
        cnt = collections.Counter()
        result = []
        for nums in nums1, nums2, nums3:
            for x in set(nums):
                cnt[x] += 1
                if cnt[x] == K:
                    result.append(x)
        return result
