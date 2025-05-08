# Time:  O(|V| + |E|)

class Solution(object):
    def eventualSafeNodes(self, graph):
        
        WHITE, GRAY, BLACK = list(range(3))

        def dfs(graph, node, lookup):
            if lookup[node] != WHITE:
                return lookup[node] == BLACK
            lookup[node] = GRAY
            if any(not dfs(graph, child, lookup) for child in graph[node]):
                return False
            lookup[node] = BLACK
            return True

        lookup = [WHITE]*len(graph)
        return [node for node in range(len(graph)) if dfs(graph, node, lookup)]
