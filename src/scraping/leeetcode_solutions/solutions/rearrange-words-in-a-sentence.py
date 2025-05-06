# Time:  O(nlogn)

class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        result = text.split()
        result[0] = result[0].lower()
        result.sort(key=len) 
        result[0] = result[0].title()
        return " ".join(result)
