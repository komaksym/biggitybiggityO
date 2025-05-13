# Time:  O(1)

class Solution(object):
    def findCenter(self, edges):
        return edges[0][edges[0][1] in edges[1]]
