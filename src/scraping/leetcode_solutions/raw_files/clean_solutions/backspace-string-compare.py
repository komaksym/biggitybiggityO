# Time:  O(m + n)

import itertools


class Solution(object):
    def backspaceCompare(self, S, T):
        def findNextChar(S):
            skip = 0
            for i in reversed(range(len(S))):
                if S[i] == 
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield S[i]

        return all(x == y for x, y in
                   itertools.zip_longest(findNextChar(S), findNextChar(T)))

