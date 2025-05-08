# Time:  O(n + k)

# prefix sum, difference array
class Solution(object):
    def minChanges(self, nums, k):
        diff = [0]*((k+1)+1)
        def update(left, right, d):
            diff[left] += d
            diff[right+1] -= d

        for i in range(len(nums)//2):
            curr = abs(nums[i]-nums[~i])
            mx = max(nums[i]-0, k-nums[i], nums[~i]-0, k-nums[~i])
            update(0, curr-1, 1)
            update(curr+1, mx, 1)
            update(mx+1, k, 2)
        result = len(nums)//2
        curr = 0
        for i in range(k+1):
            curr += diff[i]
            result = min(result, curr)
        return result
