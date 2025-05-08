# Time:  O(n)

# string
class Solution(object):
    def percentageLetter(self, s, letter):
        
        return 100*s.count(letter)//len(s)
