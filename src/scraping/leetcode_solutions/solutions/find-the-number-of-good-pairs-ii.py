# Time:  O(rlogr + n + m)

import collections


# number theory, freq table
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        cnt = [0]*(max(nums1)+1)
        for x, c in collections.Counter(k*x for x in nums2).items():
            for i in range(1, (len(cnt)-1)//x+1):
                cnt[i*x] += c
        return sum(cnt[x] for x in nums1)
