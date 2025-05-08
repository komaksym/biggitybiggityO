# Time:  O(n)
# Space: O(n)

class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))

