# Time:  O(rlogr + n + m)

import collections


# number theory, freq table
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        
        cnt = [0]*(max(nums1)+1)
        for x, c in collections.Counter(k*x for x in nums2).items():
            for i in range(1, (len(cnt)-1)//x+1):
                cnt[i*x] += c
        return sum(cnt[x] for x in nums1)


# Time:  O(n * m)
# brute force
class Solution2(object):
    def numberOfPairs(self, nums1, nums2, k):
        
        return sum(x%(k*y) == 0 for x in nums1 for y in nums2)
