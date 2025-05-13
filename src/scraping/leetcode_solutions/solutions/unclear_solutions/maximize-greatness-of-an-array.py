# Time:  O(n)

# freq table, contructive algorithms
class Solution(object):
    def maximizeGreatness(self, nums):
        return len(nums)-max(collections.Counter(nums).values())
    
    
# sort, greedy, two pointers
class Solution2(object):
    def maximizeGreatness(self, nums):
        nums.sort()
        left = 0
        for right in range(len(nums)):
            if nums[right] > nums[left]:
                left += 1
        return left
