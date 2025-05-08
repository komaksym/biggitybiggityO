# Time:  O(nlogn)

# sort, two pointers, hash table
class Solution(object):
    def distinctAverages(self, nums):
        
        lookup = set()
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            lookup.add(nums[left]+nums[right])
            left, right = left+1, right-1
        return len(lookup)
