# Time:  O(n + 26)

# hash table
class Solution(object):
    def findPermutationDifference(self, s, t):
        lookup = [-1]*26
        for i, x in enumerate(s):
            lookup[ord(x)-ord('a')] = i
        return sum(abs(lookup[ord(x)-ord('a')]-i)for i, x in enumerate(t))
