# Time:  O(n)

# hash table, constructive algorithms
class Solution(object):
    def minOperations(self, nums, k):
        
        mn = min(nums)
        return len(set(nums))-int(mn == k) if mn >= k else -1
