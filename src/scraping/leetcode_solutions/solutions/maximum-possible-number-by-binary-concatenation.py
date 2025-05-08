# Time:  O(n * logr * logn)

# sort
class Solution(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int("".join(sorted([bin(x)[2:] for x in nums], cmp=lambda x, y: (x+y > y+x)-(x+y < y+x), reverse=True)), 2)


# Time:  O(n! * nlogr)
import itertools


# brute force
class Solution2(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(int("".join(x), 2) for x in itertools.permutations([bin(x)[2:] for x in nums]))
