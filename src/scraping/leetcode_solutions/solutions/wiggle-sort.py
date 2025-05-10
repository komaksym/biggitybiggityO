# Time:  O(n)

class Solution(object):
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or \
                (not (i % 2) and nums[i - 1] < nums[i]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


# Time: O(nlogn)
class Solution2(object):
    def wiggleSort(self, nums):
        nums.sort()
        med = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]
