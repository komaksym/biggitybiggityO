# Time:  O(n)

class Solution(object):
    def numWays(self, s):
        MOD = 10**9+7

        ones = s.count('1')
        if ones % 3:
            return 0
        ones //= 3
        if ones == 0:
            return (len(s)-1)*(len(s)-2)//2 % MOD
        count = left = right = 0
        for c in s:
            if c == '1':
                count += 1
            if count == ones:
                left += 1
            elif count == 2*ones:
                right += 1
        return left*right % MOD
