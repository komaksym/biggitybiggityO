# Time:  O(n)

# two pointers, sliding window
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [-1]*(len(nums)-k+1)
        left = 0
        for right in range(len(nums)):
            if nums[right]-nums[left] != right-left:
                left = right
            if right-left+1 == k:
                result[left] = nums[right]
                left += 1
        return result


# Time:  O(n^2)
# brute force
class Solution2(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [nums[i+k-1] if all(nums[j]+1 == nums[j+1] for j in range(i, i+k-1)) else -1 for i in range(len(nums)-k+1)]
