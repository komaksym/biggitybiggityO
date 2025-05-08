# Time:  O(n)

class Solution(object):
    def findDuplicate(self, nums):
        
       
       
       
       
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# Time:  O(nlogn)
# Binary search method.
class Solution2(object):
    def findDuplicate(self, nums):
        
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
           
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Time:  O(n)
class Solution3(object):
    def findDuplicate(self, nums):
        
        duplicate = 0
       
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                break
       
        for num in nums:
            if nums[abs(num) - 1] < 0:
                nums[abs(num) - 1] *= -1
            else:
                break
        return duplicate

