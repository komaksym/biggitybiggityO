# Time:  O(n + q)

# hash table
class Solution(object):
    def matrixSumQueries(self, n, queries):
        lookup = [[False]*n for _ in range(2)]
        cnt = [0]*2
        result = 0
        for t, i, v in reversed(queries):
            if lookup[t][i]:
                continue
            lookup[t][i] = True
            cnt[t] += 1
            result += v*(n-cnt[t^1])
        return result
