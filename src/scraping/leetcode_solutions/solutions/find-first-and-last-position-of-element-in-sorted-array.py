# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(n, check): 
            left, right = 0, n-1 
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left 

        def binarySearch2(n, check): 
            left, right = 0, n 
            while left < right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid
                else:
                    left = mid+1
            return left 

        def binarySearch3(n, check): 
            left, right = -1, n-1 
            while left < right:
                mid = right - (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid
            return left+1 

        def binarySearch4(n, check): 
            left, right = -1, n 
            while right-left >= 2:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid
                else:
                    left = mid
            return left+1 

        left = binarySearch(len(nums), lambda i: nums[i] >= target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = binarySearch(len(nums), lambda i: nums[i] > target)
        return [left, right-1]
