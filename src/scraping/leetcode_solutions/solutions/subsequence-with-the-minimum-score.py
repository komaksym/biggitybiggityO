# Time:  O(n)
# Space: O(n)

# two pointers, dp
class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        right = [-1]*len(s) 
        j = len(t)-1
        for i in reversed(range(len(s))):
            if j >= 0 and t[j] == s[i]:
                j -= 1
            right[i] = j
        result = j+1
        left = 0 
        for i in range(len(s)):
            result = max(min(result, right[i]-left+1), 0)
            if left < len(t) and t[left] == s[i]:
                left += 1
        result = min(result, len(t)-left)
        return result
