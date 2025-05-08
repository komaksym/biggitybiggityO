# Time:  O(n)

import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k, n, cnts = 3, len(nums), collections.defaultdict(int)

        for i in nums:
            cnts[i] += 1
            if len(cnts) == k:
                for j in list(cnts.keys()):
                    cnts[j] -= 1
                    if cnts[j] == 0:
                        del cnts[j]

        for i in list(cnts.keys()):
            cnts[i] = 0

        for i in nums:
            if i in cnts:
                cnts[i] += 1

        result = []
        for i in list(cnts.keys()):
            if cnts[i] > n / k:
                result.append(i)

        return result

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [i[0] for i in list(collections.Counter(nums).items()) if i[1] > len(nums) / 3]

