# Time:  O(n + q)

# prefix sum
class Solution(object):
    def isArraySpecial(self, nums, queries):
        prefix = [0]*len(nums)
        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i]+int(nums[i+1]&1 != nums[i]&1)
        result = [False]*len(queries)
        for i, (l, r) in enumerate(queries):
            result[i] = prefix[r]-prefix[l] == r-l
        return result
