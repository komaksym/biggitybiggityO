# Time:  O(n)

# hash table
class Solution(object):
    def findSubarrays(self, nums):
        
        lookup = set()
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] in lookup:
                return True
            lookup.add(nums[i]+nums[i+1])
        return False
