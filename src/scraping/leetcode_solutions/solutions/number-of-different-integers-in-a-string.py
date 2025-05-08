# Time:  O(n)

class Solution(object):
    def numDifferentIntegers(self, word):
        result, num = set(), None
        for i in range(len(word)+1):
            c = word[i] if i < len(word) else ' '
            if c.isdigit():
                num = 10*num+int(c) if num is not None else int(c)
            elif num is not None:
                result.add(num)
                num = None
        return len(result)
