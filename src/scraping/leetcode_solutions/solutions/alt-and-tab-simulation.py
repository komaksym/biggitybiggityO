# Time:  O(n)

# hash table
class Solution(object):
    def simulationResult(self, windows, queries):
        lookup = [False]*len(windows)
        result = []
        for x in reversed(queries):
            if lookup[x-1]:
                continue
            lookup[x-1] = True
            result.append(x)
        result.extend(x for x in windows if not lookup[x-1])
        return result
