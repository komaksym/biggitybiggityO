# Time:  O(n^2)
# Space: O(n)

# dp
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)  # dp[j] at l: # of tuple (i, j, k) s.t. i < j < k < l and nums[i] < nums[k] < nums[j]
        result = 0
        for l in range(len(nums)):
            cnt = 0
            for j in range(l):
                if nums[j] < nums[l]:
                    cnt += 1
                    result += dp[j]
                elif nums[j] > nums[l]:
                    dp[j] += cnt
        return result

# Space: O(n^2)
# prefix sum
class Solution2(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for j in range(len(nums)):
            for i in reversed(range(j+1, len(nums))):
                right[j][i] = right[j][i+1] + int(nums[i] > nums[j])
        result = 0
        for k in range(len(nums)):
            left = 0
            for j in range(k):
                if nums[k] < nums[j]:
                    result += left*right[j][k+1]
                left += int(nums[k] > nums[j])
        return result


# Time:  O(n^2)
# Space: O(n^2)
# prefix sum
class Solution3(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for j in range(len(nums)):
            for i in range(j):
                left[j][i+1] = left[j][i] + int(nums[i] < nums[j])
        right = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for j in range(len(nums)):
            for i in reversed(range(j+1, len(nums))):
                right[j][i] = right[j][i+1] + int(nums[i] > nums[j])
        result = 0
        for k in range(len(nums)):
            for j in range(k):
                if nums[k] < nums[j]:
                    result += left[k][j]*right[j][k+1]
        return result
