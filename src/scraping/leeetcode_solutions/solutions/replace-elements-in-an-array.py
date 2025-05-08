# Time:  O(n + m)

# hash table, optimized from solution2
class Solution(object):
    def arrayChange(self, nums, operations):
        
        lookup = {x:i for i, x in enumerate(nums)}
        for x, y in operations:
            lookup[y] = lookup.pop(x)
        for x, i in lookup.items():
            nums[i] = x
        return nums


# Time:  O(n + m)
# hash table
class Solution2(object):
    def arrayChange(self, nums, operations):
        
        lookup = {x:i for i, x in enumerate(nums)}
        for x, y in operations:
            nums[lookup[x]] = y
            lookup[y] = lookup.pop(x)
        return nums
