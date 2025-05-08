# Time:  O(n)

import collections


# freq table
class Solution(object):
    def findSmallestInteger(self, nums, value):
        
        cnt = collections.Counter(x%value for x in nums)
        mn = min((cnt[i], i) for i in range(value))[1]
        return value*cnt[mn]+mn
        

# Time:  O(n)
import collections


# freq table
class Solution2(object):
    def findSmallestInteger(self, nums, value):
        
        cnt = collections.Counter(x%value for x in nums)
        for i in range(len(nums)+1):
            if not cnt[i%value]:
                return i
            cnt[i%value] -= 1
