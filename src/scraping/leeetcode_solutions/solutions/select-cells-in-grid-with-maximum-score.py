# Time:  O(n^2 * max(n, r)), r = max(x for row in grid for x in row)

# hungarian algorithm, weighted bipartite matching
class Solution(object):
    def maxScore(self, grid):
        
       
       
        def hungarian(a): 
                return 0, []
            n, m = len(a)+1, len(a[0])+1
            u, v, p, ans = [0]*n, [0]*m, [0]*m, [0]*(n-1)
            for i in range(1, n):
                p[0] = i
                j0 = 0 
                dist, pre = [float("inf")]*m, [-1]*m
                done = [False]*(m+1)
                while True: 
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
                while j0: 
                    j1 = pre[j0]
                    p[j0], j0 = p[j1], j1
            for j in range(1, m):
                if p[j]:
                    ans[p[j]-1] = j-1
            return -v[0], ans 

        mx = max(x for row in grid for x in row)
        adj = [[0]*max(mx, len(grid)) for _ in range(len(grid))]
        for i, row in enumerate(grid):
            for x in row:
                adj[i][x-1] = -x
        return -hungarian(adj)[0]


# Time:  O(r + (n * m) * 2^n), r = max(x for row in grid for x in row)
# dp, bitmasks
class Solution2(object):
    def maxScore(self, grid):
        
        mx = max(x for row in grid for x in row)
        lookup = [set() for _ in range(mx)]
        for i, row in enumerate(grid):
            for x in row:
                lookup[x-1].add(i)
        dp = [float("-inf")]*(1<<len(grid))
        dp[0] = 0
        for x in range(len(lookup)):
            if not lookup[x]:
                continue
            for mask in reversed(range(len(dp))):
                for i in lookup[x]:
                    if mask&(1<<i):
                        continue
                    dp[mask|(1<<i)] = max(dp[mask|(1<<i)], dp[mask]+(x+1))
        return max(dp)
