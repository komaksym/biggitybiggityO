# Time:  O(n)

class Solution(object):
    def minimumLength(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                break
            c = s[left]
            while left <= right:
                if s[left] != c:
                    break
                left += 1
            while left <= right:
                if s[right] != c:
                    break
                right -= 1
        return right-left+1
