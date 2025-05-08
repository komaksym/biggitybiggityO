# Time:  O(n + qlogm)

# bfs, fast exponentiation
class Solution(object):
    def queryConversions(self, conversions, queries):
        
        MOD = 10**9+7
        def divmod(a, b):
            return (a*pow(b, MOD-2, MOD))%MOD

        def unit():
            adj = [[] for _ in range(len(conversions)+1)]
            for u, v, w in conversions:
                adj[u].append((v, w))
            result = [0]*len(adj)
            result[0] = 1
            q = [0]
            while q:
                new_q = []
                for u in q:
                    for v, w in adj[u]:
                        result[v] = (result[u]*w)%MOD
                        new_q.append(v)
                q = new_q
            return result
        
        lookup = unit()
        return [divmod(lookup[b], lookup[a]) for a, b in queries]
