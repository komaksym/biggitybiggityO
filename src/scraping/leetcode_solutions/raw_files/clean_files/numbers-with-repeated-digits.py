# Time:  O(logn)

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        def P(m, n):
            result = 1
            for _ in range(n):
                result *= m
                m -= 1
            return result

        digits = list(map(int, str(N+1)))
        result = 0

        for i in range(1, len(digits)):
            result += P(9, 1)*P(9, i-1)
        prefix_set = set()
        for i, x in enumerate(digits):
            for y in range(1 if i == 0 else 0, x):
                if y in prefix_set:
                    continue
                result += P(9-i, len(digits)-i-1)
            if x in prefix_set:
                break
            prefix_set.add(x)
        return N-result
