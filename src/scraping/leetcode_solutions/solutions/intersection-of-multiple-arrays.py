# Time:  O(n * l + r), n = len(nums), l = len(nums[0])

# freq table, counting sort
class Solution(object):
    def intersection(self, nums):
        MAX_NUM = 1000
        cnt = [0]*(MAX_NUM+1)
        for num in nums:
            for x in num:
                cnt[x] += 1
        return [i for i in range(1, MAX_NUM+1) if cnt[i] == len(nums)]


# Time:  O(n * l + r), n = len(nums), l = len(nums[0]), r = max(nums)-min(nums)
# hash table, counting sort
class Solution2(object):
    def intersection(self, nums):
        result = set(nums[0])
        for i in range(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return [i for i in range(min(result), max(result)+1) if i in result] if result else []


# Time:  O(n * l + llogl), n = len(nums), l = len(nums[0])
# hash table, sort
class Solution3(object):
    def intersection(self, nums):
        result = set(nums[0])
        for i in range(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return sorted(result)
