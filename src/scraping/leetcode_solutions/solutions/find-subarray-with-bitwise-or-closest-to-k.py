# Time:  O(nlogr), r = max(nums)

# freq table, two pointers, sliding window, lc1521
class BitCount(object):
    def __init__(self, n):
        self.__l = 0
        self.__n = n
        self.__count = [0]*n
    
    def __iadd__(self, num):
        self.__l += 1
        base = 1
        for i in range(self.__n):
            if num&base:
                self.__count[i] += 1
            base <<= 1
        return self

    def __isub__(self, num):
        self.__l -= 1
        base = 1
        for i in range(self.__n):
            if num&base:
                self.__count[i] -= 1
            base <<= 1
        return self

    def bit_or(self):
        num, base = 0, 1
        for i in range(self.__n):
            if self.__count[i]:
                num |= base
            base <<= 1
        return num

                    
class Solution(object):
    def minimumDifference(self, nums, k):
        count = BitCount(max(nums).bit_length())
        result, left = float("inf"), 0
        for right in range(len(nums)):
            count += nums[right]
            while left <= right:
                f = count.bit_or()
                result = min(result, abs(f-k))
                if f <= k:
                    break
                count -= nums[left]
                left += 1
        return result


# Time:  O(nlogr), r = max(nums)
# dp, lc1521
class Solution2(object):
    def minimumDifference(self, nums, k):
        result, dp = float("inf"), set() 
        for x in nums:
            dp = {x}|{f|x for f in dp}
            for f in dp:
                result = min(result, abs(f-k))
        return result
    
