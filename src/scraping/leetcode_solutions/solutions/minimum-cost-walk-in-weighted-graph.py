# Time:  O(n + e + q)

# union find
class Solution(object):
    def minimumCost(self, n, edges, query):
        class UnionFind(object): 
            def __init__(self, n):
                self.set = list(range(n))
                self.rank = [0]*n
                self.w = [-1]*n 

            def find_set(self, x):
                stk = []
                while self.set[x] != x: 
                    stk.append(x)
                    x = self.set[x]
                while stk:
                    self.set[stk.pop()] = x
                return x

            def union_set(self, x, y, w): 
                x, y = self.find_set(x), self.find_set(y)
                if x == y:
                    self.w[x] &= w 
                    return False
                if self.rank[x] > self.rank[y]: 
                    x, y = y, x
                self.set[x] = self.set[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
                self.w[y] &= self.w[x]&w 
                return True
            
            def cost(self, x): 
                return self.w[self.find_set(x)]

        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union_set(u, v, w)
        result = [-1]*(len(query))
        for i, (s, t) in enumerate(query):
            if uf.find_set(s) != uf.find_set(t):
                continue
            result[i] = uf.cost(s) if s != t else 0
        return result
