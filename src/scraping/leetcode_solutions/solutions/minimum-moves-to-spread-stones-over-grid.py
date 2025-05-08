# Time:  O(max(x^2 * y)) = O(n^3), n = len(grid)*len(grid[0]), y = len(zero), x = n-y

# weighted bipartite matching solution
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def hungarian(a):  # Time: O(n^2 * m), Space: O(n + m)
            if not a:
                return 0, []
            n, m = len(a)+1, len(a[0])+1
            u, v, p, ans = [0]*n, [0]*m, [0]*m, [0]*(n-1)
            for i in range(1, n):
                p[0] = i
                j0 = 0  # add "dummy" worker 0
                dist, pre = [float("inf")]*m, [-1]*m
                done = [False]*(m+1)
                while True:  # dijkstra
                    done[j0] = True
                    i0, j1, delta = p[j0], None, float("inf")
                    for j in range(1, m):
                        if done[j]:
                            continue
                        cur = a[i0-1][j-1]-u[i0]-v[j]
                        if cur < dist[j]:
                            dist[j], pre[j] = cur, j0
                        if dist[j] < delta:
                            delta, j1 = dist[j], j
                    for j in range(m):
                        if done[j]:
                            u[p[j]] += delta
                            v[j] -= delta
                        else:
                            dist[j] -= delta
                    j0 = j1
                    if not p[j0]:
                        break
                while j0:  # update alternating path
                    j1 = pre[j0]
                    p[j0], j0 = p[j1], j1
            for j in range(1, m):
                if p[j]:
                    ans[p[j]-1] = j-1
            return -v[0], ans  # min cost

        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        src, dst = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]-1 >= 0:
                    src.extend([(i, j)]*(grid[i][j]-1))
                else:
                    dst.append((i, j))
        adj = [[dist(src[i], dst[j]) for j in range(len(dst))] for i in range(len(src))]
        return hungarian(adj)[0]


# Time:  O(max(x^2 * y)) = O(n^2), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
from scipy.optimize import linear_sum_assignment as hungarian
import itertools


# 3rd-party weighted bipartite matching solution
class Solution2(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        src, dst = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]-1 >= 0:
                    src.extend([(i, j)]*(grid[i][j]-1))
                else:
                    dst.append((i, j))
        adj = [[dist(src[i], dst[j]) for j in range(len(dst))] for i in range(len(src))]
        return sum(adj[i][j] for i, j in zip(*hungarian(adj)))    


# Time:  O(max(x^y)) = O((n/2)^(n/2))) = O(5^5), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
# backtracking
class Solution3(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        def backtracking(curr):
            if curr == len(zero):
                return 0
            result = float("inf")
            i, j = zero[curr]
            for ni in range(len(grid)):
                for nj in range(len(grid[0])):
                    if not (grid[ni][nj] >= 2):
                        continue
                    grid[ni][nj] -= 1
                    result = min(result, dist((i, j), (ni, nj))+backtracking(curr+1))
                    grid[ni][nj] += 1
            return result

        zero = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
        return backtracking(0)
