# Time:  O(n)

# greedy
class Solution(object):
    def addMinimum(self, word):
        
        return 3*(sum(i-1 < 0 or word[i-1] >= word[i] for i in range(len(word))))-len(word)
 
