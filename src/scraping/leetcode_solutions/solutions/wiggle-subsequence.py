# Time:  O(n)

class Solution(object):
    def wiggleMaxLength(self, nums):
        
        if len(nums) < 2:
            return len(nums)

        length, up = 1, None

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i] and (up is None or up is False):
                length += 1
                up = True
            elif nums[i - 1] > nums[i] and (up is None or up is True):
                length += 1
                up = False

        return length

