# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def maxScore(self, nums):
        
        nums.sort(reverse=True)
        curr = 0
        for i, x in enumerate(nums):
            curr += x
            if curr <= 0:
                return i
        return len(nums)
