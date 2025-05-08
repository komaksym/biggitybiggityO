# Time:  O(n^3)

class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def floydWarshall(n, graph): 
            reachable = set([x[0]*n+x[1] for x in graph]) 
            for k in range(n): 
                for i in range(n): 
                    for j in range(n): 
                        if i*n+j not in reachable and (i*n+k in reachable and k*n+j in reachable):
                            reachable.add(i*n+j)
            return reachable

        reachable = floydWarshall(n, prerequisites)
        return [i*n+j in reachable for i, j in queries]


# Time:  O(n * q)
import collections


class Solution2(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtyp
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        result = []
        for i, j in queries:
            stk, lookup = [i], set([i])
            while stk:
                node = stk.pop()
                for nei in graph[node]:
                    if nei in lookup:
                        continue
                    stk.append(nei)
                    lookup.add(nei)
            result.append(j in lookup)
        return result
