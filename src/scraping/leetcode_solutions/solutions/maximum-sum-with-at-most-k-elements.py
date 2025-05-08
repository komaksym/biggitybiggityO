# Time:  O(n * m)

import random


# greedy, quick select
class Solution(object):
    def maxSum(self, grid, limits, k):
        
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else: 
                    left = pivot_right+1

        candidates = []
        for i in range(len(grid)):
            cnt = min(k, limits[i])
            nth_element(grid[i], cnt-1, lambda a, b: a > b)
            for j in range(cnt):
                candidates.append(grid[i][j])
        nth_element(candidates, k-1, lambda a, b: a > b)
        return sum(candidates[i] for i in range(k))
