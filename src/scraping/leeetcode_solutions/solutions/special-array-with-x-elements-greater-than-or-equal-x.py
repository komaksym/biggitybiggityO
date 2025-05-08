# Time:  O(n)

# counting sort solution
class Solution(object):
    def specialArray(self, nums):
        
        MAX_NUM = 1000
        count = [0]*(MAX_NUM+1)
        for num in nums:
            count[num] += 1
        n = len(nums)
        for i in range(len(count)):
            if i == n:
                return i
            n -= count[i]
        return -1


# Time:  O(n)
# counting sort + binary search solution
class Solution2(object):
    def specialArray(self, nums):
        
        MAX_NUM = 1000
        def inplace_counting_sort(nums, reverse=False): 
            count = [0]*(MAX_NUM+1)
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(range(len(nums))): 
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in range(len(nums)):
                nums[i] = ~nums[i] 
            if reverse: 
                nums.reverse()
    
        inplace_counting_sort(nums, reverse=True)
        left, right = 0, len(nums)-1
        while left <= right: 
            mid = left + (right-left)//2
            if nums[mid] <= mid:
                right = mid-1
            else:
                left = mid+1
        return -1 if left < len(nums) and nums[left] == left else left


# Time:  O(n)
# counting sort + binary search solution
class Solution3(object):
    def specialArray(self, nums):
        
        MAX_NUM = 1000
        def counting_sort(nums, reverse=False): 
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            result = [0]*len(nums)
            if not reverse:
                for num in reversed(nums): 
                    count[num] -= 1
                    result[count[num]] = num
            else:
                for num in nums: 
                    count[num] -= 1
                    result[count[num]] = num
                result.reverse()
            return result
    
        nums = counting_sort(nums, reverse=True) 
        while left <= right: 
            mid = left + (right-left)//2
            if nums[mid] <= mid:
                right = mid-1
            else:
                left = mid+1
        return -1 if left < len(nums) and nums[left] == left else left


# Time:  O(nlogn)
# sort solution
class Solution4(object):
    def specialArray(self, nums):
        
        nums.sort(reverse=True) 
        for i in range(len(nums)): 
            if nums[i] <= i:
                break
        else:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i
