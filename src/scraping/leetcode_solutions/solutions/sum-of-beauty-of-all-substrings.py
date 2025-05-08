# Time:  O(n^2)

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0 
        for i in range(len(s)):
            lookup = [0]*26
            for j in range(i, len(s)):
                lookup[ord(s[j])-ord('a')] += 1
                result += max(lookup) - min(x for x in lookup if x)
        return result
