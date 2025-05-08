# Time:  O(n)

class Solution(object):
    def minTimeToType(self, word):
        
        return (min((ord(word[0])-ord('a'))%26, (ord('a')-ord(word[0]))%26)+1) + \
               sum(min((ord(word[i])-ord(word[i-1]))%26, (ord(word[i-1])-ord(word[i]))%26)+1
                   for i in range(1, len(word)))
