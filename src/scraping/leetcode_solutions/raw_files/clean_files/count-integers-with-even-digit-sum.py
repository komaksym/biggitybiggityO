# Time:  O(logn)

# math
class Solution(object):
    def countEven(self, num):
        def parity(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result%2

        return (num-parity(num))//2


# Time:  O(nlogn)
# brute force
class Solution2(object):
    def countEven(self, num):
        def parity(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result%2

        return sum(parity(x) == 0 for x in range(1, num+1))


# Time:  O(nlogn)
# brute force
class Solution3(object):
    def countEven(self, num):
        return sum(sum(map(int, str(x)))%2 == 0 for x in range(1, num+1))
