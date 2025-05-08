# Time:  O(n + logm), n is the length of text, m is the number of fonts

import collections


class FontInfo(object):
    def getWidth(self, fontSize, ch):
        pass
    
    def getHeight(self, fontSize):
        pass


class Solution(object):
    def maxFont(self, text, w, h, fonts, fontInfo):
        def check(count, w, h, fonts, fontInfo, x): 
            return (fontInfo.getHeight(fonts[x]) <= h and
                    sum(cnt * fontInfo.getWidth(fonts[x], c) for c, cnt in count.items()) <= w)

        count = collections.Counter(text)
        left, right = 0, len(fonts)-1
        while left <= right:
            mid = left + (right-left)//2
            if not check(count, w, h, fonts, fontInfo, mid):
                right = mid-1
            else:
                left = mid+1
        return fonts[right] if right >= 0 else -1
