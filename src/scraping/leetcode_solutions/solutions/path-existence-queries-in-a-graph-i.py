# Time:  O(n + q)

# prefix sum
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        
        prefix = [0]*n
        for i in range(n-1):
            prefix[i+1] = prefix[i]+int(nums[i+1]-nums[i] > maxDiff)
        return [prefix[i] == prefix[j] for i, j in queries]
