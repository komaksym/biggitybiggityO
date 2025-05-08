# Time:  O(n)

class Solution(object):
    def findPermutation(self, s):
        
        result = []
        for i in range(len(s)+1):
            if i == len(s) or s[i] == 'I':
                result += list(range(i+1, len(result), -1))
        return result

