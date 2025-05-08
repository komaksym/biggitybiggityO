# Time:  O(d), d is the number of digits

# greedy, counting sort
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        def inplace_counting_sort(nums, reverse=False): 
            count = [0]*(max(nums)+1)
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

        sign = 1 if num >= 0 else -1
        nums = list(map(int, list(str(abs(num)))))
        inplace_counting_sort(nums, reverse=(sign == -1))
        i = next((i for i in range(len(nums)) if nums[i] != 0), 0)
        nums[0], nums[i] = nums[i], nums[0]
        return sign*int("".join(map(str, nums)))


# Time:  O(dlogd), d is the number of digits
# greedy
class Solution2(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        sign = 1 if num >= 0 else -1
        nums = sorted(str(abs(num)), reverse=(sign == -1))
        i = next((i for i in range(len(nums)) if nums[i] != '0'), 0)
        nums[0], nums[i] = nums[i], nums[0]
        return sign*int("".join(nums))
