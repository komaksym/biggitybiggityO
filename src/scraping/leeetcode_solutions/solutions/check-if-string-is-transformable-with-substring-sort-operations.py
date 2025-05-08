# Time:  O(n)

class Solution(object):
    def isTransformable(self, s, t):
        
        idxs = [[] for _ in range(10)]
        for i in reversed(range(len(s))):
            idxs[int(s[i])].append(i)
        for c in t:
            d = int(c)
            if not idxs[d]:
                return False
            for k in range(d): 
                if idxs[k] and idxs[k][-1] < idxs[d][-1]:
                    return False
            idxs[d].pop()
        return True
