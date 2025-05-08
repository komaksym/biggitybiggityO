# Time:  O(nlogn + n * r), r = max(e for _, e in tasks)

# sort, greedy
class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1])
        lookup = set()
        for s, e, d in tasks:
            d -= sum(i in lookup for i in range(s, e+1))
            for i in reversed(range(1, e+1)):
                if d <= 0:
                    break
                if i in lookup:
                    continue
                lookup.add(i)
                d -= 1
        return len(lookup)
