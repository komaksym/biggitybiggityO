# Time:  O(logn)

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, total = 1, 0
        while n:
            n, r = divmod(n, 10)
            product *= r
            total += r
        return product-total


# Time:  O(logn)
import operator
from functools import reduce


class Solution2(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        A = list(map(int, str(n)))
        return reduce(operator.mul, A) - sum(A)
