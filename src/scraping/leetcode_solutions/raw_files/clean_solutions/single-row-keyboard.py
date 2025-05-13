# Time:  O(n)

class Solution(object):
    def calculateTime(self, keyboard, word):
        lookup = {c:i for i, c in enumerate(keyboard)}
        result, prev = 0, 0
        for c in word:
            result += abs(lookup[c]-prev)
            prev = lookup[c]
        return result
