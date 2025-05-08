# Time:  O(n)

import itertools


class Solution(object):
    def magicalString(self, n):
        
        def gen(): 
            for c in 1, 2, 2:
                yield c
            for i, c in enumerate(gen()):
                if i > 1:
                    for _ in range(c):
                        yield i % 2 + 1

        return sum(c & 1 for c in itertools.islice(gen(), n))

