# Time:  O(e)

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        
        result = []
        lookup = set()
        for u, v in edges:
            lookup.add(v)
        for i in range(n):
            if i not in lookup:
                result.append(i)
        return result
