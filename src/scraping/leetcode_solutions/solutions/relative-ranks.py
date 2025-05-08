# Time:  O(nlogn)

class Solution(object):
    def findRelativeRanks(self, nums):
        
        sorted_nums = sorted(nums)[::-1]
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, list(range(4, len(nums) + 1))))
        return list(map(dict(list(zip(sorted_nums, ranks))).get, nums))

