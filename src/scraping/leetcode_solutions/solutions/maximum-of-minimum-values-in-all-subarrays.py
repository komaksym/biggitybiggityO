# Time:  O(n)

class Solution(object):
    def findMaximums(self, nums):
        
        def find_bound(nums, direction, init):
            result = [0]*len(nums)
            stk = [init]
            for i in direction(range(len(nums))):
                while stk[-1] != init and nums[stk[-1]] >= nums[i]:
                    stk.pop()
                result[i] = stk[-1]
                stk.append(i)
            return result

        left = find_bound(nums, lambda x: x, -1)
        right = find_bound(nums, reversed, len(nums))
        result = [-1]*len(nums)
        for i, v in enumerate(nums):
            result[((right[i]-1)-left[i])-1] = max(result[((right[i]-1)-left[i])-1], v)
        for i in reversed(range(len(nums)-1)):
            result[i] = max(result[i], result[i+1])
        return result
