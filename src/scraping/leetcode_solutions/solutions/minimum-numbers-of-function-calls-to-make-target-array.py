# Time:  O(nlogn)

class Solution(object):
    def minOperations(self, nums):
        
        def popcount(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        result, max_len = 0, 1
        for num in nums:
            result += popcount(num)
            max_len = max(max_len, num.bit_length())
        return result + (max_len-1)
