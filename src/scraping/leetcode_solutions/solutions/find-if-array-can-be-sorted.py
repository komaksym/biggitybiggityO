# Time:  O(n)
# Space: O(1)

# sort
class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count("1")
    
        left = mx = 0
        for right in range(len(nums)):
            if right+1 != len(nums) and popcount(nums[right+1]) == popcount(nums[right]):
                continue
            if mx > min(nums[i] for i in range(left, right+1)):
                return False
            mx = max(nums[i] for i in range(left, right+1))
            left = right+1
        return True


# Time:  O(n)
# Space: O(n)
import itertools


# sort
class Solution2(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count("1")
        
        def pairwise(it):
            a, b = tee(it)
            next(b, None)
            return zip(a, b)

        return all(max(a) <= min(b) for a, b in pairwise(list(it) for key, it in groupby(nums, popcount)))


# Time:  O(nlogn)
# Space: O(n)
# sort
class Solution3(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count("1")
    
        left = 0
        for right in range(len(nums)):
            if right+1 != len(nums) and popcount(nums[right+1]) == popcount(nums[right]):
                continue
            nums[left:right+1] = sorted(nums[left:right+1])
            left = right+1
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
