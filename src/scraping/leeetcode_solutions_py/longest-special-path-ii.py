# Time:  O(n + e)
# Space: O(n + e)

import collections


# iterative dfs, two pointers, sliding window, prefix sum
class Solution(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        def iter_dfs():
            result = [float("inf")]*2
            lookup = collections.defaultdict(lambda: -1)
            prefix = [0]
            stk = [(1, (0, -1, 0, [-1]*2))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, d, left = args
                    prev_d, lookup[nums[u]-1] = lookup[nums[u]-1], d
                    new_left = left[:]
                    curr = prev_d
                    for i in range(len(new_left)):
                        if curr > new_left[i]:
                            curr, new_left[i] = new_left[i], curr
                    result = min(result, [-(prefix[(d-1)+1]-prefix[new_left[1]+1]), d-new_left[1]])
                    stk.append((4, (u, prev_d)))
                    stk.append((2, (u, p, d, new_left, 0)))
                elif step == 2:
                    u, p, d, left, i = args
                    if i == len(adj[u]):
                        continue
                    stk.append((2, (u, p, d, left, i+1)))
                    v, l = adj[u][i]
                    if v == p:
                        continue
                    prefix.append(prefix[-1]+l)
                    stk.append((3, None))
                    stk.append((1, (v, u, d+1, left)))
                elif step == 3:
                    prefix.pop()
                elif step == 4:
                    u, prev_d = args
                    lookup[nums[u]-1] = prev_d
            return [-result[0], result[1]]
    
        adj = [[] for _ in range(len(nums))]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))        
        return iter_dfs()


# Time:  O(n + e)
# Space: O(h)
import collections


# dfs, two pointers, sliding window, prefix sum
class Solution2(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        def dfs(u, p, d, left):
            prev_d, lookup[nums[u]-1] = lookup[nums[u]-1], d
            new_left = left[:]
            curr = prev_d
            for i in range(len(new_left)):
                if curr > new_left[i]:
                    curr, new_left[i] = new_left[i], curr
            result[0] = min(result[0], [-(prefix[(d-1)+1]-prefix[new_left[1]+1]), d-new_left[1]])
            for v, l in adj[u]:
                if v == p:
                    continue
                prefix.append(prefix[-1]+l)
                dfs(v, u, d+1, new_left)
                prefix.pop()
            lookup[nums[u]-1] = prev_d
    
        adj = [[] for _ in range(len(nums))]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))
        lookup = collections.defaultdict(lambda: -1)
        prefix = [0]
        result = [[float("inf"), float("inf")]]
        dfs(0, -1, 0, [-1]*2)
        return [-result[0][0], result[0][1]]
