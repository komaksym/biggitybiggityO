# Time:  O(n * l)

# string
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        return [w for word in words for w in word.split(separator) if w]
