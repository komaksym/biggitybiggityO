# Time:  O(n)

# freq table
class Solution(object):
    def edgeScore(self, edges):
        score = [0]*len(edges)
        for u, v in enumerate(edges):
            score[v] += u
        return max(range(len(edges)), key=lambda x:score[x])
    
