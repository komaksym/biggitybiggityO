# Time:  O(nlogn)

# greedy, sort
class Solution(object):
    def maxPrice(self, items, capacity):
        result = 0
        items.sort(key=lambda x: float(x[0])/x[1], reverse=True)
        for p, c in items:
            cnt = min(c, capacity)
            capacity -= cnt
            result += (float(p)/c)*cnt
        return result if capacity == 0 else -1
