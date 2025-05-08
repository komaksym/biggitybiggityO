# Time:  O(n)

class Solution(object):
    def minFlips(self, s):
        
        result = float("inf")
        cnt1 = cnt2 = 0
        for i in range(2*len(s)-1 if len(s)%2 else len(s)):
            if i >= len(s):
                cnt1 -= int(s[i%len(s)])^((i-len(s))%2)^0
                cnt2 -= int(s[i%len(s)])^((i-len(s))%2)^1
            cnt1 += int(s[i%len(s)])^(i%2)^0
            cnt2 += int(s[i%len(s)])^(i%2)^1
            if i >= len(s)-1:
                result = min(result, cnt1, cnt2)
        return result
