# Time:  O(n)

# string
class Solution(object):
    def divideString(self, s, k, fill):
        return [s[i:i+k] + fill*(i+k-len(s)) for i in range(0, len(s), k)]
