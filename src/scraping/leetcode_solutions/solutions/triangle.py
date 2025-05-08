from functools import reduce
# Time:  O(m * n)

class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        cur = triangle[0] + [float("inf")]
        for i in range(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in range(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [float("inf")]

        return reduce(min, cur)

