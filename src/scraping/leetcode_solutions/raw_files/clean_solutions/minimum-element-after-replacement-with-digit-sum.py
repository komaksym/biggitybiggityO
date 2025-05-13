# Time:  O(nlogr)

# array
class Solution(object):
    def minElement(self, nums):
        def f(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result

        return min(f(x) for x in nums)
