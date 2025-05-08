# Time:  O(m * n)

class Solution(object):
    def matrixReshape(self, nums, r, c):
        
        if not nums or \
           r*c != len(nums) * len(nums[0]):
            return nums

        result = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                result[count/c][count%c] = nums[i][j]
                count += 1
        return result

