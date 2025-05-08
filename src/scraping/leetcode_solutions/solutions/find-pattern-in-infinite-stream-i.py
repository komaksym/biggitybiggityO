# Time:  O(p + n)

class InfiniteStream:
    def __next__(self):
        pass


# kmp
class Solution(object):
    def findPattern(self, stream, pattern):
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = getPrefix(pattern)
        i = j = -1
        while True:
            d = next(stream)
            i += 1
            while j+1 > 0 and pattern[j+1] != d:
                j = prefix[j]
            if pattern[j+1] == d:
                j += 1
            if j+1 == len(pattern):
                return i-j
        return -1
