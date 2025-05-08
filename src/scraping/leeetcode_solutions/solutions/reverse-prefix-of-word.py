# Time:  O(n)

class Solution(object):
    def reversePrefix(self, word, ch):
        
        i = word.find(ch)
        return word[:i+1][::-1]+word[i+1:]
