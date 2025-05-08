# Time:  O(n)

# prefix sum, CodeChef Starters 146 - Bouncing Ball (https://www.codechef.com/problems/BOUNCE_BALL)
class Solution(object):
    def countValidSelections(self, nums):
        total = sum(nums)
        result = curr = 0
        for x in nums:
            if not x:
                result += max(2-abs(curr-(total-curr)), 0)
            else:
                curr += x
        return result


# Time:  O(n)
# prefix sum, CodeChef Starters 146 - Bouncing Ball (https://www.codechef.com/problems/BOUNCE_BALL)
class Solution2(object):
    def countValidSelections(self, nums):
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        suffix = [0]*(len(nums)+1)
        for i in reversed(range(len(nums))):
            suffix[i] = suffix[i+1]+nums[i]
        return sum(max(2-abs(prefix[i]-suffix[i+1]), 0) for i in range(len(nums)) if nums[i] == 0)
