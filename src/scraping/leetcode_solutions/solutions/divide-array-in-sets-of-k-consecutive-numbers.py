# Time:  O(nlogn)

import collections


class Solution(object):
    def isPossibleDivide(self, nums, k):
        
        count = collections.Counter(nums)
        for num in sorted(count.keys()):
            c = count[num]
            if not c:
                continue
            for i in range(num, num+k):
                if count[i] < c:
                    return False
                count[i] -= c
        return True
