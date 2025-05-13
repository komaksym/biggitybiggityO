# Time:  O(log(min(m, n)))

# gcd-like solution
class Solution(object):
    def countOperations(self, num1, num2):
        result = 0
        while num2:
            result += num1//num2
            num1, num2 = num2, num1%num2
        return result
