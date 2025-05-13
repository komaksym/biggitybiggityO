# Time:  O(logn)

# greedy
class Solution(object):
    def smallestNumber(self, n):
        result = []
        for d in reversed(range(2, 9+1)):
            while n%d == 0:
                result.append(d)
                n //= d
        return "".join(map(str, reversed(result))) or "1" if n == 1 else "-1"
