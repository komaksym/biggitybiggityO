# Time:  O(logn)

import bisect


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        
        i = bisect.bisect_right(letters, target)
        return letters[0] if i == len(letters) else letters[i]

