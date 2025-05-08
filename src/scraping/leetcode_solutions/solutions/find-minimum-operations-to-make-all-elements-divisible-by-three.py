# Time:  O(n)

# math
class Solution(object):
    def minimumOperations(self, nums):
        
        return sum(x%3 != 0 for x in nums)


# Time:  O(n)
# math
class Solution2(object):
    def minimumOperations(self, nums):
        
        return sum(min(x%3, 3-x%3) for x in nums)
