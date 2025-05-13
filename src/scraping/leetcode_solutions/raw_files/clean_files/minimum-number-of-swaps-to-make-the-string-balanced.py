# Time:  O(n)

class Solution(object):
    def minSwaps(self, s):
        result = curr = 0
        for c in s:
            if c == ']':
                curr += 1
                result = max(result, curr)
            else:
                curr -= 1
        return (result+1)//2
