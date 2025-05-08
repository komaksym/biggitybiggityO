# Time:  O(n)

import heapq
import collections


# partial sort, freq table
class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        def check(cnt2, cnt1):
            return all(cnt1.get(k, 0)-v >= 0 for k, v in cnt2.items())  # for python2
            
        mx = max(nums2)
        cnt2 = collections.Counter(nums2)
        return next(d for d in [mx-x for x in heapq.nlargest(3, nums1)] if check(cnt2, collections.Counter(x+d for x in nums1)))


# Time:  O(n)
import collections


# partial sort, freq table
class Solution2(object):
    def minimumAddedInteger(self, nums1, nums2):
        def check(cnt2, cnt1):
            return all(cnt1.get(k, 0)-v >= 0 for k, v in cnt2.items())  # for python2
        
        def topk(a, k):  # Time: O(k * n)
            result = [float("-inf")]*k
            for x in a:
                for i in range(len(result)):
                    if x > result[i]:
                        result[i], x = x, result[i]
            return result
    
        mx = max(nums2)
        cnt2 = collections.Counter(nums2)
        return next(d for d in [mx-x for x in topk(nums1, 3)] if check(cnt2, collections.Counter(x+d for x in nums1)))


# Time:  O(nlogn)
# sort
class Solution3(object):
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        for i in range(3):
            d = nums2[-1]-nums1[~i]
            cnt = 0
            for j in range(len(nums2)):
                while j+cnt < len(nums1) and nums1[j+cnt]+d != nums2[j]:
                    cnt += 1
            if cnt <= 2:
                return d
        return -1
