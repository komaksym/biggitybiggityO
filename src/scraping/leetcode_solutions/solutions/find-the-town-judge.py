# Time:  O(t + n)

class Solution(object):
    def findJudge(self, N, trust):
        
        degrees = [0]*N
        for i, j in trust:
            degrees[i-1] -= 1
            degrees[j-1] += 1
        for i in range(len(degrees)):
            if degrees[i] == N-1:
                return i+1
        return -1
