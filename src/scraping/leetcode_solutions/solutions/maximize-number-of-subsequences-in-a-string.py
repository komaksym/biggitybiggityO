# Time:  O(n)

# counting, greedy
class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        
        result = cnt1 = cnt2 = 0
        for c in text:
            if c == pattern[1]:
                result += cnt1
                cnt2 += 1
            if c == pattern[0]:
                cnt1 += 1
        return result + max(cnt1, cnt2) 
