# Time:  O(n)

# greedy, lc1526
class Solution(object):
    def minimumOperations(self, nums, target):
        
        for i in range(len(target)):
            target[i] -= nums[i]
        return sum(max((target[i] if i < len(target) else 0)-(target[i-1] if i-1 >= 0 else 0), 0) for i in range(len(target)+1))
