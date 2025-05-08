# Time:  O(n)

class Solution(object):
    def findContestMatch(self, n):
        
        matches = list(map(str, list(range(1, n+1))))
        while len(matches)/2:
            matches = ["({},{})".format(matches[i], matches[-i-1]) for i in range(len(matches)/2)]
        return matches[0]


