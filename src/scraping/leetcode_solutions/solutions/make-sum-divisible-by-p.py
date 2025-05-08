# Time:  O(n)

class Solution(object):
    def minSubarray(self, nums, p):
        
        residue = sum(nums) % p
        if not residue:
            return 0
        result = len(nums)
        curr, lookup = 0, {0: -1}
        for i, num in enumerate(nums):
            curr = (curr+num) % p
            lookup[curr] = i
            if (curr-residue) % p in lookup:
                result = min(result, i-lookup[(curr-residue)%p])
        return result if result < len(nums) else -1
