# Time:  O(n + klogn)
# Space: O(1)

import heapq


# heap
class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        result = 0
        for i, x in enumerate(nums):
            nums[i] = -x
        heapq.heapify(nums)
        for _ in range(k):
            if not nums:
                break
            x = -heapq.heappop(nums)
            result += x
            nx = ceil_divide(x, 3)
            if not nx:
                continue
            heapq.heappush(nums, -nx)
        return result
# Space: O(1)
import heapq


# heap
class Solution2(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        result = 0
        for i, x in enumerate(nums):
            nums[i] = -x
        heapq.heapify(nums)
        for _ in range(k):
            x = -heapq.heappop(nums)
            result += x
            heapq.heappush(nums, -ceil_divide(x, 3))
        return result
  
