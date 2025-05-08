# Time:  O(n^2 * 2^n)

# brute force, bitmask
class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        def check(mask):
            return all(((mask>>j)&1) == statements[i][j]
                       for i in range(len(statements)) if (mask>>i)&1 
                       for j in range(len(statements[i])) if statements[i][j] != 2)

        def popcount(x):
            result = 0
            while x:
                x &= x-1
                result += 1
            return result

        result = 0
        for mask in range(1<<len(statements)):
            if check(mask):
                result = max(result, popcount(mask))
        return result
