# Time:  O(n)

class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)
        for x in citations:
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1

        h = 0
        for i in reversed(range(0, n + 1)):
            h += count[i]
            if h >= i:
                return i
        return h

# Time:  O(nlogn)
class Solution2(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h

# Time:  O(nlogn)
class Solution3(object):
    def hIndex(self, citations):
        return sum(x >= i + 1 for i, x in enumerate(sorted(citations, reverse=True)))


