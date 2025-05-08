# Time:  O(|V|^3)

class Solution(object):
    def numberOfPaths(self, n, corridors):
        
        adj = [set() for _ in range(n)]
        for u, v in corridors:
            adj[min(u, v)-1].add(max(u, v)-1)
        return sum(k in adj[i] for i in range(n) for j in adj[i] for k in adj[j])
