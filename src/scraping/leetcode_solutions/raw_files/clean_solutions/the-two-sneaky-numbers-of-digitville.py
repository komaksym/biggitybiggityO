# Time:  O(n)

import itertools
from functools import reduce


# bit manipulation
class Solution(object):
    def getSneakyNumbers(self, nums):
        def f(check):
            return reduce(lambda accu, x: accu^x, (x for x in itertools.chain(nums, range(n)) if check(x)), 0)

        n = len(nums)-2
        x_xor_y = f(lambda _: True)
        bit = x_xor_y&-x_xor_y
        return [f(lambda x: x&bit == 0), f(lambda x: x&bit != 0)]
