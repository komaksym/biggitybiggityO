# Time:  O(n)

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return 1+max(s.count(' ') for s in sentences)
