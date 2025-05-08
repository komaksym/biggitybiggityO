# Time:  O(n)

import collections


class Solution(object):
    def longestSubsequence(self, arr, difference):
        
        result = 1
        lookup = collections.defaultdict(int)
        for i in range(len(arr)):
            lookup[arr[i]] = lookup[arr[i]-difference] + 1
            result = max(result, lookup[arr[i]])
        return result
