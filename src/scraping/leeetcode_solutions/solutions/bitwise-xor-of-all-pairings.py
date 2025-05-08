# Time:  O(n)

import operator
from functools import reduce


# bit manipulation
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        
        return (reduce(operator.xor, nums1) if len(nums2)%2 else 0) ^ \
               (reduce(operator.xor, nums2) if len(nums1)%2 else 0)
