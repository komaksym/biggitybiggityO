# Time:  O(n)

import collections


class Solution(object):
    def maxNumberOfBalloons(self, text):
        
        TARGET = "balloon"
        source_count = collections.Counter(text)
        target_count = collections.Counter(TARGET)
        return min(source_count[c]//target_count[c] for c in target_count.keys())
