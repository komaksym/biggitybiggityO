# Time:  O(n^2)
# Space: O(1)

# dp
class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        n = len(fruits)
        for i in range(n):
            for j in range(i+1, n-(i+1)):
                fruits[i][j] = 0
        for i in range(1, n-1):
            for j in range(i+1, n):
                fruits[i][j] += max(fruits[i-1][j-1], fruits[i-1][j], fruits[i-1][j+1] if j+1 < n else 0)
        for j in range(n):
            for i in range(j+1, n-(j+1)):
                fruits[i][j] = 0
        for j in range(1, n-1):
            for i in range(j+1, n):
                fruits[i][j] += max(fruits[i-1][j-1], fruits[i][j-1], fruits[i+1][j-1] if i+1 < n else 0)
        return sum(fruits[i][i] for i in range(n))+fruits[-2][-1]+fruits[-1][-2]
    
