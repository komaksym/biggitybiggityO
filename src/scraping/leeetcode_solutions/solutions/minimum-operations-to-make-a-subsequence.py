# Time:  O(nlogn)

import bisect


class Solution(object):
    def minOperations(self, target, arr):
        
        lookup = {x:i for i, x in enumerate(target)}
        lis = []
        for x in arr:
            if x not in lookup:
                continue
            i = bisect.bisect_left(lis, lookup[x])
            if i == len(lis):
                lis.append(lookup[x])
            else:
                lis[i] = lookup[x]
        return len(target)-len(lis)
    
    
# Range Maximum Query
class SegmentTree(object): 
    def __init__(self, N,
                 build_fn=lambda x, y: [y]*(2*x),
                 query_fn=lambda x, y: y if x is None else max(x, y), 
                 update_fn=lambda x, y: y,
                 default_val=0):
        self.N = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.default_val = default_val
        self.tree = build_fn(N, default_val)
        self.lazy = [None]*N

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def update(self, L, R, h): 
            while x > 1:
                x //= 2
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1: 
                self.__apply(L, h) 
                L += 1
            if R & 1 == 0: 
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R): 
            n = 2**self.H
            while n != 1:
                y = x // n
                if self.lazy[y] is not None:
                    self.__apply(y*2, self.lazy[y])
                    self.__apply(y*2 + 1, self.lazy[y])
                    self.lazy[y] = None
                n //= 2

        result = None
        if L > R:
            return result

        L += self.N
        R += self.N
        push(L)
        push(R)
        while L <= R:
            if L & 1: 
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0: 
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result
    
    def __str__(self):
        showList = []
        for i in range(self.N):
            showList.append(self.query(i, i))
        return ",".join(map(str, showList))


# Time:  O(nlogn)
# segment tree solution
class Solution2(object):
    def minOperations(self, target, arr):
        
        lookup = {x:i for i, x in enumerate(target)}
        st = SegmentTree(len(lookup))
        for x in arr:
            if x not in lookup:
                continue
            st.update(lookup[x], lookup[x], st.query(0, lookup[x]-1)+1 if lookup[x] >= 1 else 1)
        return len(target)-(st.query(0, len(lookup)-1) if len(lookup) >= 1 else 0)
