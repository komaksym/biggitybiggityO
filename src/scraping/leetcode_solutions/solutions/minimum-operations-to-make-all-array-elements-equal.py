# Time:  O(nlogn + qlogn)

# sort, binary search, prefix sum
class Solution(object):
    def minOperations(self, nums, queries):
        
        nums.sort()
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        result = [0]*len(queries)
        for i, q in enumerate(queries):
            j = bisect.bisect_left(nums, q)
            result[i] = (q*j-prefix[j])+((prefix[-1]-prefix[j])-q*(len(nums)-j))
        return result
