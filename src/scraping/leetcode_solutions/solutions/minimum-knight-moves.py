# Time:  O(1)
# Space: O(1)

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        lookup = {(1, 0):3, (2, 2):4}  # special cases
        if (x, y) in lookup:
            return lookup[(x, y)]
        k = x-y
        if y > k:
            return k - 2*((k-y)//3)
        return k - 2*((k-y)//4)


# Time:  O(n^2)
# Space: O(n^2)
class Solution2(object):
    def __init__(self):
        self.__lookup = {(0, 0):0, (1, 1):2, (1, 0):3}  # special cases

    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def dp(x, y):
            x, y = abs(x), abs(y)
            if x < y:
                x, y = y, x
            if (x, y) not in self.__lookup:  # greedy, smaller x, y is always better if not special cases
                self.__lookup[(x, y)] = min(dp(x-1, y-2), dp(x-2, y-1)) + 1
            return self.__lookup[(x, y)]
        return dp(x, y)
