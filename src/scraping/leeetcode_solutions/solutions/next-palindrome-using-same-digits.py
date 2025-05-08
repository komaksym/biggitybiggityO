# Time:  O(n)

class Solution(object):
    def nextPalindrome(self, num):
        
        def next_permutation(nums, begin, end):
            def reverse(nums, begin, end):
                left, right = begin, end-1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            k, l = begin-1, begin
            for i in reversed(range(begin, end-1)):
                if nums[i] < nums[i+1]:
                    k = i
                    break
            else:
                reverse(nums, begin, end)
                return False
            for i in reversed(range(k+1, end)):
                if nums[i] > nums[k]:
                    l = i
                    break
            nums[k], nums[l] = nums[l], nums[k]
            reverse(nums, k+1, end)
            return True
        
        nums = list(num)
        if not next_permutation(nums, 0, len(nums)//2):
            return ""
        for i in range(len(nums)//2):
            nums[-1-i] = nums[i]
        return "".join(nums)
