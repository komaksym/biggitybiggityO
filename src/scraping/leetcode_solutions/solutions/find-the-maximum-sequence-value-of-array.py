# Time:  O(n * r + r^2)

# bitmasks, prefix sum, dp
class Solution(object):
    def maxValue(self, nums, k):
        
        INF = float("inf")
        MAX_MASK = 127
        def is_submask(a, b):
            return (a|b) == b

        def dp(direction, npos):
            result = [npos]*(MAX_MASK+1)
            dp = [INF]*(MAX_MASK+1)
            cnt = [0]*(MAX_MASK+1)
            for i in direction(range(len(nums))):
                dp[nums[i]] = 1
                for mask in range(MAX_MASK+1):
                    if is_submask(nums[i], mask):
                        cnt[mask] += 1
                    dp[mask|nums[i]] = min(dp[mask|nums[i]], dp[mask]+1)
                for mask in range(MAX_MASK+1):
                    if cnt[mask] >= k and dp[mask] <= k and result[mask] == npos:
                        result[mask] = i
            return result

        left = dp(lambda x: x, len(nums))
        right = dp(reversed, -1)
        return next(result for result in reversed(range(MAX_MASK+1)) for l in range(1, MAX_MASK+1) if left[l] < right[result^l])


# Time:  O(n * k * r + n * r^2)
# prefix sum, dp
class Solution(object):
    def maxValue(self, nums, k):
        
        left = [[set() if j else {0} for j in range(k+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            for j in range(1, len(left[i+1])):
                left[i+1][j] = set(left[i][j])
                for x in left[i][j-1]:
                    left[i+1][j].add(x|nums[i])
        right = [[set() if j else {0} for j in range(k+1)] for i in range(len(nums)+1)]
        for i in reversed(range(len(nums))):
            for j in range(1, len(right[i])):
                right[i][j] = set(right[i+1][j])
                for x in right[i+1][j-1]:
                    right[i][j].add(x|nums[i])
        return max(l^r for i in range(k, (len(nums)-k)+1) for l in left[i][k] for r in right[i][k])
