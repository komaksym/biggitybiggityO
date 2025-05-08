# Time:  O(n)

# bitmasks, hash table
class Solution(object):
    def smallestSubarrays(self, nums):
        
        result = [0]*len(nums)
        lookup = [-1]*max(max(nums).bit_length(), 1)
        for i in reversed(range(len(nums))):
            for bit in range(len(lookup)):
                if nums[i]&(1<<bit):
                    lookup[bit] = i
            result[i] = max(max(lookup)-i+1, 1)
        return result
