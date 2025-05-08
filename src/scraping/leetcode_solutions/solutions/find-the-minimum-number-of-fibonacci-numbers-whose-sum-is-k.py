# Time:  O(logk)

class Solution(object):
    def findMinFibonacciNumbers(self, k):
        result, a, b = 0, 1, 1
        while b <= k:
            b, a = a+b, b
        while k:
            if a <= k:
                k -= a
                result += 1
            a, b = b-a, a
        return result
