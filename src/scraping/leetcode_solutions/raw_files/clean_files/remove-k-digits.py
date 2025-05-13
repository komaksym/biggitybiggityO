# Time:  O(n)

class Solution(object):
    def removeKdigits(self, num, k):
        result = []
        for d in num:
            while k and result and result[-1] > d:
                result.pop()
                k -= 1
            result.append(d)
        return ''.join(result).lstrip('0')[:-k or None] or '0'

