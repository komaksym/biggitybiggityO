# Time:  O(logn)
# Space: O(1)

# reference: https://en.wikipedia.org/wiki/Gray_code
class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gray_to_binary(n):
            result = 0
            while n:
                result ^= n
                n >>= 1
            return result
        return gray_to_binary(n)


# Time:  O(logn)
# Space: O(1)
class Solution2(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result = -result - (n^(n-1))  # 2^(pos[i]+1)-1
            n &= n-1
        return abs(result)
