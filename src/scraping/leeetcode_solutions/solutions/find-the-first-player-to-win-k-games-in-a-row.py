# Time:  O(n)

# simulation
class Solution(object):
    def findWinningPlayer(self, skills, k):
        
        result = cnt = 0
        for i in range(1, len(skills)):
            if skills[result] < skills[i]:
                result = i
                cnt = 0
            cnt += 1
            if cnt == k:
                return result
        return result
