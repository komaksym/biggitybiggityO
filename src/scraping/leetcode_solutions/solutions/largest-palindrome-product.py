# Time:  O(n * 10^n)
# Space: O(n)

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upper = 10**n-1
        for k in range(2, upper+1):
            left = 10**n-k
            right = int(str(left)[::-1])
            d = k**2-right*4
            if d < 0:
                continue
            if d**0.5 == int(d**0.5) and k%2 == int(d**0.5)%2:
                return (left*10**n+right)%1337
        return -1


# Time:  O(10^(2n))
# Space: O(n)
class Solution2(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def divide_ceil(a, b):
            return (a+b-1)//b

        if n == 1:
            return 9
        upper, lower = 10**n-1, 10**(n-1)
        for i in reversed(range(lower, upper**2//(10**n)+1)):
            candidate = int(str(i) + str(i)[::-1])
            for y in reversed(range(divide_ceil(lower, 11)*11, upper+1, 11)): 
                if candidate//y > upper:
                    break
                if candidate%y == 0 and lower <= candidate//y:
                    return candidate%1337
        return -1
