# Time:  O(n^3)

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [set() for _ in range(n+1)]
        degree = [0]*(n+1)
        for u, v in edges:
            adj[min(u, v)].add(max(u, v))
            degree[u] += 1
            degree[v] += 1
        result = float("inf")
        for u in range(1, n+1):
            for v in adj[u]:
                for w in adj[u]:
                    if v < w and w in adj[v]:
                        result = min(result, degree[u]+degree[v]+degree[w] - 6)
        return result if result != float("inf") else -1
