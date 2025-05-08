# Time:  O(n * (1 + 1/4 + 1/9 + ... + 1/x^2)) = O(pi^2 / 6 * n) = O(n), see https://en.wikipedia.org/wiki/Basel_problem

# number theory, basel problem
class Solution(object):
    def maximumSum(self, nums):
        
        return max(sum(nums[i*x**2-1] for x in range(1, int((len(nums)//i)**0.5)+1)) for i in range(1, len(nums)+1))
