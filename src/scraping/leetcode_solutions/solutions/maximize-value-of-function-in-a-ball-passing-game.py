# Time:  O(n)

import collections


# graph, prefix sum, two pointers, sliding window
class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        
        def find_cycles(adj):
            result = []
            lookup = [0]*len(adj)
            idx = 0
            for u in range(len(adj)):
                prev = idx
                while not lookup[u]:
                    idx += 1
                    lookup[u] = idx
                    u = adj[u]
                if lookup[u] > prev:
                    result.append((u, idx-lookup[u]+1))
            return result

        def find_prefixes():
            lookup = [(-1, -1)]*len(receiver)
            prefixes = [[0] for _ in range(len(cycles))]
            for idx, (u, l) in enumerate(cycles):
                for i in range(l):
                    lookup[u] = (idx, i)
                    prefixes[idx].append(prefixes[idx][i]+u)
                    u = receiver[u]
            return lookup, prefixes
        
        def get_sum(prefix, i, cnt):
            l = len(prefix)-1
            q, r = divmod(cnt, l)
            return (q*prefix[-1]+
                    (prefix[min(i+r, l)]-prefix[i])+
                    (prefix[max(((i+r)-l, 0))]-prefix[0]))
        
        def start_inside_cycle():
            result = 0
            for u, l in cycles:
                for _ in range(l):
                    idx, i = lookup[u]
                    result = max(result, get_sum(prefixes[idx], i, k+1))
                    u = receiver[u]
            return result
    
        def start_outside_cycle():
            result = 0
            degree = [0]*len(receiver)
            for x in receiver:
                degree[x] += 1
            for u in range(len(receiver)):
                if degree[u]:
                    continue
                curr = 0
                dq = collections.deque()
                while lookup[u][0] == -1:
                    curr += u
                    dq.append(u)
                    if len(dq) == k+1:
                        result = max(result, curr)
                        curr -= dq.popleft()
                    u = receiver[u]
                idx, i = lookup[u]
                while dq:
                    result = max(result, curr+get_sum(prefixes[idx], i, (k+1)-len(dq)))
                    curr -= dq.popleft()
            return result
            
        cycles = find_cycles(receiver)
        lookup, prefixes = find_prefixes()
        return max(start_inside_cycle(), start_outside_cycle())


# Time:  O(nlogk)
# binary lifting
class Solution2(object):
    def getMaxFunctionValue(self, receiver, k):
        
        l = (k+1).bit_length()
        P = [receiver[:] for _ in range(l)]
        S = [list(range(len(receiver))) for _ in range(l)]
        for i in range(1, len(P)):
            for u in range(len(receiver)):
                P[i][u] = P[i-1][P[i-1][u]]
                S[i][u] = S[i-1][u]+S[i-1][P[i-1][u]]
        result = 0
        for u in range(len(receiver)):
            curr = 0
            for i in range(l):
                if (k+1)&(1<<i):
                    curr += S[i][u]
                    u = P[i][u]
            result = max(result, curr)
        return result
