# Time:  O(n)

# two pointers, greedy
class Solution(object):
    def appendCharacters(self, s, t):
        
        i = -1
        for j, c in enumerate(t):
            for i in range(i+1, len(s)):
                if s[i] == c:
                    break
            else:
                return len(t)-j
        return 0
