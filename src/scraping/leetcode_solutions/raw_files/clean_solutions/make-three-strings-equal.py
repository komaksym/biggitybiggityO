# Time:  O(n)

import itertools


# string
class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        for i, (a, b, c) in enumerate(zip(s1, s2, s3)):
            if not a == b == c:
                break
        else:
            i += 1
        return len(s1)+len(s2)+len(s3)-3*i if i else -1
