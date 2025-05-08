# Time:  O(n)

class Solution(object):
    def shuffle(self, nums, n):
        
        def index(i):
            return 2*i if i < n else 2*(i-n)+1
    
        for i in range(len(nums)):
            j = i
            while nums[i] >= 0:
                j = index(j)
                nums[i], nums[j] = nums[j], ~nums[i] 
        for i in range(len(nums)):
            nums[i] = ~nums[i]
        return nums
