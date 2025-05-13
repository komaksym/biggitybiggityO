# Time:  ctor:         O(|V| + |E|)
#        addEdge:      O(1)
#        shortestPath: O((|E| + |V|) * log|V|) = O(|E| * log|V|)

import heapq


# dijkstra's algorithm
class Solution(object):

    def __init__(self, n, edges):
        self.__adj = [[] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge):
        u, v, w = edge
        self.__adj[u].append((v, w))

    def shortestPath(self, node1, node2):
        def dijkstra(adj, start, target):
            best = [float("inf")]*len(adj)
            best[start] = 0
            min_heap = [(best[start], start)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr > best[u]:
                    continue
                for v, w in adj[u]:                
                    if not (curr+w < best[v]):
                        continue
                    best[v] = curr+w
                    heapq.heappush(min_heap, (best[v], v))
            return best[target] if best[target] != float("inf") else -1

        return dijkstra(self.__adj, node1, node2)
