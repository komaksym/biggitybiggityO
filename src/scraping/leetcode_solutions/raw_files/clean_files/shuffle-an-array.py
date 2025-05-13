# Time:  O(n)

import random


class Solution(object):

    def __init__(self, nums):
        self.__nums = nums


    def reset(self):
        return self.__nums


    def shuffle(self):
        nums = list(self.__nums)
        for i in range(len(nums)):
            j = random.randint(i, len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums



