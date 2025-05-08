# Time:  O(n)

import collections


class Solution(object):
    def maxResult(self, nums, k):
        
        score = 0
        dq = collections.deque()
        for i, num in enumerate(nums):
            if dq and dq[0][0] == i-k-1:
                dq.popleft()
            score = num if not dq else dq[0][1]+num
            while dq and dq[-1][1] <= score:
                dq.pop()
            dq.append((i, score))
        return score
