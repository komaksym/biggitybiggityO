# Time:  O(m + n)
# Space: O(1)

import collections


class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        count1 = collections.Counter(ord(c)-ord('a') for c in a)
        count2 = collections.Counter(ord(c)-ord('a') for c in b)
        result = len(a) + len(b) - max((count1+count2).values()) 
        for i in range(26-1):
            if i > 0:
                count1[i] += count1[i-1]
                count2[i] += count2[i-1]
            result = min(result, len(a) - count1[i] + count2[i]) 
            result = min(result, len(b) - count2[i] + count1[i]) 
        return result
