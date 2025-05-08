# Time:  O(nlogn)

class Solution(object):
    def arrayRankTransform(self, arr):
        
        return list(map({x: i+1 for i, x in enumerate(sorted(set(arr)))}.get, arr))
