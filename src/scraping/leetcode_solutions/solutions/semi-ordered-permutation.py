# Time:  O(n)

# greedy
class Solution(object):
    def semiOrderedPermutation(self, nums):
        
        i, j = nums.index(1), nums.index(len(nums))
        return i+((len(nums)-1)-j)-int(i > j)
