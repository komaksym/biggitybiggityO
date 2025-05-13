# Time:  O(nlogr) = O(n)

class Solution(object):
    def selfDividingNumbers(self, left, right):
        def isDividingNumber(num):
            n = num
            while n > 0:
                n, r = divmod(n, 10)
                if r == 0 or (num%r) != 0:
                    return False
            return True
        
        return [num for num in range(left, right+1) if isDividingNumber(num)]


# Time:  O(nlogr) = O(n)
import itertools


class Solution2(object):
    def selfDividingNumbers(self, left, right):
        return [num for num in range(left, right+1) \
                if not any(map(lambda x: int(x) == 0 or num%int(x) != 0, str(num)))]
