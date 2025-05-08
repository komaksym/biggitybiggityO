# Time:  O(m * n * sqrt(m * n))

# the problem is the same as google codejam 2008 round 3 problem C
# https://github.com/kamyu104/GoogleCodeJam-2008/blob/master/Round%203/no_cheating.py

import collections


from functools import partial

# Time:  O(E * sqrt(V))
# Source code from http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
def bipartiteMatch(graph):
    
    
   
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    
    while 1:
       
       
       
       
       
        preds = {}
        unmatched = []
        pred = dict([(u,unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        
       
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        
       
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))

       
       
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0
        
        def recurse_iter(v):
            def divide(v):
                if v not in preds:
                    return
                L = preds[v]
                del preds[v]
                for u in L :
                    if u in pred and pred[u] is unmatched: 
                        del pred[u]
                        matching[v] = u
                        ret[0] = True
                        return
                stk.append(partial(conquer, v, iter(L)))

            def conquer(v, it):
                for u in it:
                    if u not in pred:
                        continue
                    pu = pred[u]
                    del pred[u]
                    stk.append(partial(postprocess, v, u, it))
                    stk.append(partial(divide, pu))
                    return

            def postprocess(v, u, it):
                if not ret[0]:
                    stk.append(partial(conquer, v, it))
                    return
                matching[v] = u

            ret, stk = [False], []
            stk.append(partial(divide, v))
            while stk:
                stk.pop()()
            return ret[0]

        for v in unmatched: recurse_iter(v)


# Hopcroft-Karp bipartite matching
class Solution(object):
    def maxStudents(self, seats):
        
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        E, count = collections.defaultdict(list), 0
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] != '.':
                    continue
                count += 1
                if j%2:
                    continue
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < len(seats) and \
                       0 <= nj < len(seats[0]) and \
                       seats[ni][nj] == '.':
                        E[i*len(seats[0])+j].append(ni*len(seats[0])+nj)
        return count-len(bipartiteMatch(E)[0])


# Time:  O(|V| * |E|) = O(m^2 * n^2)
# Hungarian bipartite matching
class Solution2(object):
    def maxStudents(self, seats):
        
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        def dfs(seats, e, lookup, matching):
            i, j = e
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0 <= ni < len(seats) and 0 <= nj < len(seats[0]) and \
                    seats[ni][nj] == '.' and not lookup[ni][nj]:
                    lookup[ni][nj] = True
                    if matching[ni][nj] == -1 or dfs(seats, matching[ni][nj], lookup, matching):
                        matching[ni][nj] = e
                        return True
            return False
        
        def Hungarian(seats):
            result = 0
            matching = [[-1]*len(seats[0]) for _ in range(len(seats))]
            for i in range(len(seats)):
                for j in range(0, len(seats[0]), 2):
                    if seats[i][j] != '.':
                        continue
                    lookup = [[False]*len(seats[0]) for _ in range(len(seats))]
                    if dfs(seats, (i, j), lookup, matching):
                        result += 1
            return result
          
        count = 0
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == '.':
                    count += 1
        return count-Hungarian(seats)


# Time:  O(m * 2^n * 2^n) = O(m * 4^n)
# dp solution
class Solution3(object):
    def maxStudents(self, seats):
        
        def popcount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result
        
        dp = {0: 0}
        for row in seats:
            invalid_mask = sum(1 << c for c, v in enumerate(row) if v == 
            new_dp = {}
            for mask1, v1 in dp.items():
                for mask2 in range(1 << len(seats[0])):
                    if (mask2 & invalid_mask) or \
                       (mask2 & (mask1 << 1)) or (mask2 & (mask1 >> 1)) or \
                       (mask2 & (mask2 << 1)) or (mask2 & (mask2 >> 1)):
                        continue
                    new_dp[mask2] = max(new_dp.get(mask2, 0), v1+popcount(mask2))
            dp = new_dp
        return max(dp.values()) if dp else 0
