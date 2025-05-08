# Time:  O(n + klogk), k is the distinct number of changed

class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed)%2:
            return []
        cnts = collections.Counter(changed)
        for x in sorted(cnts.keys()):
            if cnts[x] > cnts[2*x]:
                return []
            cnts[2*x] -= cnts[x] if x else cnts[x]//2
        return list(cnts.elements())
