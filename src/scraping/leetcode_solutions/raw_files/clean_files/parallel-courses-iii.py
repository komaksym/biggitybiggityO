# Time:  O(|V| + |E|)

class Solution(object):
    def minimumTime(self, n, relations, time):
        adj = [[] for _ in range(n)]
        in_degree = [0]*n
        for prev, nxt in relations:
            adj[prev-1].append(nxt-1)
            in_degree[nxt-1] += 1
        q = [u for u in range(n) if not in_degree[u]]
        dist = [time[u] if not in_degree[u] else 0 for u in range(n)] 
        while q:
            new_q = []
            for u in q:
                for v in adj[u]:
                    dist[v] = max(dist[v], dist[u]+time[v])
                    in_degree[v] -= 1
                    if not in_degree[v]:
                        new_q.append(v)
            q = new_q
        return max(dist)
