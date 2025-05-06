# Time:  O(n * l^4)

import collections


# freq table, combinatorics
class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 7
        POW10 = [0]*L
        POW10[0] = 1
        for i in range(L-1):
            POW10[i+1] = POW10[i]*10
        cnt1 = collections.Counter(nums)
        adj = collections.defaultdict(list)
        cnt = list(cnt1.items())
        for idx in range(len(cnt)):
            adj[cnt[idx][0]].append(idx)
            for i in range(L):
                a = cnt[idx][0]//POW10[i]%10
                for j in range(i+1, L):
                    b = cnt[idx][0]//POW10[j]%10
                    if a == b:
                        continue
                    adj[cnt[idx][0]-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j])].append(idx)
        result = sum(v*(v-1)//2 for v in cnt1.values())
        lookup = set()
        for u in adj.keys():
            for i in range(len(adj[u])):
                v1 = cnt[adj[u][i]][1]
                for j in range(i+1, len(adj[u])):
                    v2 = cnt[adj[u][j]][1]
                    if (adj[u][i], adj[u][j]) in lookup:
                        continue
                    lookup.add((adj[u][i], adj[u][j]))
                    result += v1*v2
        return result


# Time:  O(n * l^(2 * k)) = O(n * l^4)
import collections


# freq table, combinatorics, bfs
class Solution2(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 7
        K = 2
        POW10 = [0]*L
        POW10[0] = 1
        for i in range(L-1):
            POW10[i+1] = POW10[i]*10
        def at_most(k, x):
            lookup = {x}
            result = [x]
            u = 0
            for _ in range(k):
                for u in range(u, len(result)):
                    x = result[u]
                    for i in range(L):
                        a = x//POW10[i]%10
                        for j in range(i+1, L):
                            b = x//POW10[j]%10
                            if a == b:
                                continue
                            y = x-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j])
                            if y in lookup:
                                continue
                            lookup.add(y)
                            result.append(y)
            return result

        result = 0
        cnt1 = collections.Counter(nums)
        cnt2 = collections.Counter()
        for x, v in cnt1.items():
            result += cnt2[x]*v+v*(v-1)//2
            for x in at_most(K, x):
                if x not in cnt1:
                    continue
                cnt2[x] += v
        return result
