# Time:  O(n)

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        def stoi(s):
            result = 0
            for c in s:
                result = result*10 + ord(c)-ord('a')
            return result
        
        return stoi(firstWord) + stoi(secondWord) == stoi(targetWord)
