# Time:  O(n)

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        
        left = 0
        for right in range(len(s)):
            maxCost -= abs(ord(s[right])-ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left])-ord(t[left]))
                left += 1
        return (right+1)-left
