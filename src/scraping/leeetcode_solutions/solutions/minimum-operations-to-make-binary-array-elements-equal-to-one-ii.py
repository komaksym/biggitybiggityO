# Time:  O(n)

# greedy
class Solution(object):
    def minOperations(self, nums):
        
        result = 0
        for x in nums:
            if x^(result&1):
                continue
            result += 1
        return result
