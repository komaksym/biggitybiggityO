# Time:  O(n)

class Solution(object):
    def isGoodArray(self, nums):
        
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

       
        result = nums[0]
        for num in nums:
            result = gcd(result, num)
            if result == 1:
                break
        return result == 1
