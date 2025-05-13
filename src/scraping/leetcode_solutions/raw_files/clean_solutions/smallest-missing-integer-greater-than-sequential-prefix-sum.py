# Time:  O(n)

# hash table
class Solution(object):
    def missingInteger(self, nums):
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                break
            total += nums[i]
        lookup = set(nums)
        while total in lookup:
            total += 1
        return total
