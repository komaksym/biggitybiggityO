# Time:  O(n)

class Solution(object):
    def find132pattern(self, nums):
        ak = float("-inf")
        stk = []
        for i in reversed(range(len(nums))):
            if nums[i] < ak:
                return True
            while stk and stk[-1] < nums[i]:
                ak = stk.pop()
            stk.append(nums[i])
        return False


# Time:  O(n^2)
class Solution_TLE(object):
    def find132pattern(self, nums):
        for k in range(len(nums)):
            valid = False
            for j in range(k):
                if nums[j] < nums[k]:
                    valid = True
                elif nums[j] > nums[k]:
                    if valid:
                        return True
        return False
