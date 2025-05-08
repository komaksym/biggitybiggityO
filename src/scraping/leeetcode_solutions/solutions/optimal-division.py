# Time:  O(n)

class Solution(object):
    def optimalDivision(self, nums):
        
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        result = [str(nums[0]) + "/(" + str(nums[1])]
        for i in range(2, len(nums)):
            result += "/" + str(nums[i])
        result += ")"
        return "".join(result)

