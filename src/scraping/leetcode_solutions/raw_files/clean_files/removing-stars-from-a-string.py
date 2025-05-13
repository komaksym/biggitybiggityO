# Time:  O(n)

# stack
class Solution(object):
    def removeStars(self, s):
        result = []
        for c in s:
            if c == '*':
                result.pop()
            else:
                result.append(c)
        return "".join(result)
