# Time:  O(n)

# graph, hash table
class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        def dfs(node):
            lookup = {}
            i = 0
            while node != -1:
                if node in lookup:
                    break
                lookup[node] = i
                i += 1
                node = edges[node]
            return lookup
        
        lookup1, lookup2 = dfs(node1), dfs(node2)
        intersect = set(lookup1.keys())&set(lookup2.keys())
        return min(intersect, key=lambda x: (max(lookup1[x], lookup2[x]), x)) if intersect else -1
