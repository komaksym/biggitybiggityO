# Time:  O(n^3)

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float("inf")]*n for _ in range(n)]
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0
        for k in range(n): 
            for i in range(n): 
                for j in range(n): 
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]) 
        result = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return result[min(result.keys())]
