# Time:  O(nlogx), x is the max denominator

import re


class Solution(object):
    def fractionAddition(self, expression):
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        ints = list(map(int, re.findall('[+-]?\d+', expression)))
        A, B = 0, 1
        for i in range(0, len(ints), 2):
            a, b = ints[i], ints[i+1]
            A = A * b + a * B
            B *= b
            g = gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)

