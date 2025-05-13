# Time:  O(nlog(logm)), n the length of nums, m is the max value of nums

import bisect


class Solution(object):
    def __init__(self):
        M = 10**5
        self.__lookup = [0]
        i = 10
        while i < M:
            self.__lookup.append(i)
            i *= 10
        self.__lookup.append(i)

    def findNumbers(self, nums):
        def digit_count(n):
            return bisect.bisect_right(self.__lookup, n)

        return sum(digit_count(n) % 2 == 0 for n in nums)
class Solution2(object):
    def findNumbers(self, nums):
        def digit_count(n):
            result = 0
            while n:
                n //= 10
                result += 1
            return result

        return sum(digit_count(n) % 2 == 0 for n in nums)


# Time:  O(nlogm), n the length of nums, m is the max value of nums
class Solution3(object):
    def findNumbers(self, nums):
        return sum(len(str(n)) % 2 == 0 for n in nums)
