# Time:  O(n)

class Solution(object):
    def countLetters(self, S):
        
        result = len(S)
        left = 0
        for right in range(1, len(S)):
            if S[right] == S[left]:
                result += right-left
            else:
                left = right
        return result
