# Time:  O(n)

import itertools


# greedy
class Solution(object):
    def minOperations(self, nums1, nums2, k):
        
        cnt1 = cnt2 = 0
        for x, y in zip(nums1, nums2):
            if y == x:
                continue
            if k == 0 or (y-x)%k:
                return -1
            if x < y:
                cnt1 += (y-x)//k
            else:
                cnt2 += (x-y)//k
        return cnt1 if cnt1 == cnt2 else -1
