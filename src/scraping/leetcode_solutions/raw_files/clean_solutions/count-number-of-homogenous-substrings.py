# Time:  O(n)

class Solution(object):
    def countHomogenous(self, s):
        MOD = 10**9+7
        result = cnt = 0
        for i in range(len(s)):
            if i and s[i-1] == s[i]:
                cnt += 1
            else:
                cnt = 1
            result = (result+cnt)%MOD
        return result
