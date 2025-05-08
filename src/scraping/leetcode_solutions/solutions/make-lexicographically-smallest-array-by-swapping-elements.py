# Time:  O(nlogn)

# sort
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x])
        groups = []
        for i in range(len(nums)):
            if i-1 < 0 or nums[idxs[i]]-nums[idxs[i-1]] > limit:
                groups.append([])
            groups[-1].append(idxs[i])
        result = [-1]*len(nums)
        for g in groups:
            for i, j in enumerate(sorted(g)):
                result[j] = nums[g[i]]
        return result
