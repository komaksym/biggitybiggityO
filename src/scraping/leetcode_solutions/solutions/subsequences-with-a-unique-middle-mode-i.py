# Time:  O(n)

import collections


# freq table, prefix sum, combinatorics
class Solution(object):
    def subsequencesWithMiddleMode(self, nums):
        def nC2(x):
            return x*(x-1)//2

        MOD = 10**9+7
        result = 0
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        for x in nums:
            right[x] += 1
        left_x_sq = 0 
        right_x_sq = sum(v**2 for v in right.values()) 
        left_x_right_x = 0 
        left_x_sq_right_x = 0 
        left_x_right_x_sq = 0 
        for i, v in enumerate(nums):
            left_x_sq -= left[v]**2
            right_x_sq -= right[v]**2
            left_x_right_x -= left[v]*right[v]
            left_x_sq_right_x -= left[v]**2*right[v]
            left_x_right_x_sq -= left[v]*right[v]**2
            right[v] -= 1

            l, r = i, len(nums)-(i+1)
            result += nC2(l)*nC2(r)
            result -= nC2(l-left[v])*nC2(r-right[v])
            result -= ((left_x_sq-(l-left[v]))*(r-right[v])-(left_x_sq_right_x-left_x_right_x))*right[v]//2
            result -= ((right_x_sq-(r-right[v]))*(l-left[v])-(left_x_right_x_sq-left_x_right_x))*left[v]//2
            result -= left[v]*left_x_right_x*(r-right[v])-left[v]*left_x_right_x_sq
            result -= right[v]*left_x_right_x*(l-left[v])-right[v]*left_x_sq_right_x
            result -= right[v]*(left_x_sq_right_x-left_x_right_x)//2
            result -= left[v]*(left_x_right_x_sq-left_x_right_x)//2

            left[v] += 1
            left_x_sq += left[v]**2
            right_x_sq += right[v]**2
            left_x_right_x += left[v]*right[v]
            left_x_sq_right_x += left[v]**2*right[v]
            left_x_right_x_sq += left[v]*right[v]**2
        return result % MOD
