# Time:  O(n)

# hash table
class Solution(object):
    def minOperations(self, nums, k):
        lookup = [False]*k
        for i in reversed(range(len(nums))):
            if nums[i] > len(lookup) or lookup[nums[i]-1]:
                continue
            lookup[nums[i]-1] = True
            k -= 1
            if not k:
                break
        return len(nums)-i
