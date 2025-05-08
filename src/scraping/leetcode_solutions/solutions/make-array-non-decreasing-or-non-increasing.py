# Time:  O(nlogn)

import heapq


# greedy, heap
class Solution(object):
    def convertArray(self, nums):
        
        def f(nums):
            result = 0
            max_heap = []
            for x in nums:
                if max_heap and x < -max_heap[0]:
                    result += -heapq.heappop(max_heap)-x
                    heapq.heappush(max_heap, -x)
                heapq.heappush(max_heap, -x)
            return result
        
        return min(f(nums), f((x for x in reversed(nums))))


# Time:  O(n^2)
import collections


# dp
class Solution2(object):
    def convertArray(self, nums):
        
        vals = sorted(set(nums))
        def f(nums):
            dp = collections.defaultdict(int) 
            for x in nums:
                prev = -1
                for i in vals:
                    dp[i] = min(dp[i]+abs(i-x), dp[prev]) if prev != -1 else dp[i]+abs(i-x)
                    prev = i
            return dp[vals[-1]]

        return min(f(nums), f((x for x in reversed(nums))))
