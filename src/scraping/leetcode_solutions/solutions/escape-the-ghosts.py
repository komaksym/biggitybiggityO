# Time:  O(n)

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        
        total = abs(target[0])+abs(target[1])
        return all(total < abs(target[0]-i)+abs(target[1]-j) for i, j in ghosts)

