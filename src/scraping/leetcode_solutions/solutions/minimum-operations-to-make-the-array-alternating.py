# Time:  O(n)
# Space: O(n)
import collections


# freq table
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_top = collections.Counter(nums[i] for i in range(0, len(nums), 2)).most_common(2) 
        odd_top = collections.Counter(nums[i] for i in range(1, len(nums), 2)).most_common(2) 
        if not odd_top or even_top[0][0] != odd_top[0][0]:
            return len(nums)-even_top[0][1]-(odd_top[0][1] if odd_top else 0)
        return min(len(nums)-even_top[0][1]-(odd_top[1][1] if len(odd_top) == 2 else 0),
                   len(nums)-odd_top[0][1]-(even_top[1][1] if len(even_top) == 2 else 0))
