# Time:  O(logn)

# combinatorics
class Solution(object):
    def countSpecialNumbers(self, n):
        
        def P(m, n):
            result = 1
            for _ in range(n):
                result *= m
                m -= 1
            return result

        digits = list(map(int, str(n+1)))
        result = sum(P(9, 1)*P(9, i-1) for i in range(1, len(digits)))
        lookup = set()
        for i, x in enumerate(digits):
            for y in range(int(i == 0), x):
                if y in lookup:
                    continue
                result += P(9-i, len(digits)-i-1)
            if x in lookup:
                break
            lookup.add(x)
        return result
