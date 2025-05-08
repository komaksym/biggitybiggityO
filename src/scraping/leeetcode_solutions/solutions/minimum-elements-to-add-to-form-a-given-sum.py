# Time:  O(n)

class Solution(object):
    def minElements(self, nums, limit, goal):
        
        return (abs(sum(nums)-goal) + (limit-1))//limit
