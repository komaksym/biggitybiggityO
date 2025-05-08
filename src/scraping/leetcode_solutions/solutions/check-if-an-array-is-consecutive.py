# Time:  O(n)

# hash table
class Solution(object):
    def isConsecutive(self, nums):
        return max(nums)-min(nums)+1 == len(nums) == len(set(nums))


# Time:  O(nlogn)
# sort
class Solution2(object):
    def isConsecutive(self, nums):
        nums.sort()
        return all(nums[i]+1 == nums[i+1] for i in range(len(nums)-1))
