# Time:  O(n)

# hash table
class Solution(object):
    def minimumOperations(self, nums):
        return len({x for x in nums if x})
