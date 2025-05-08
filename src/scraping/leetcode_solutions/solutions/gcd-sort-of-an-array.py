# Time:  O(nlogn + n * α(n) + m * log(logm)) ~= O(nlogn + m), m is the max of nums

import itertools


class UnionFind(object):  # Time: O(n * α(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = list(map(self.find_set, (x, y)))
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:  # union by rank
            self.set[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.set[y_root] = x_root
        else:
            self.set[y_root] = x_root
            self.rank[x_root] += 1
        return True


class Solution(object):
    def gcdSort(self, nums):
        def modified_sieve_of_eratosthenes(n, lookup, uf):  # Time: O(n * log(logn)), Space: O(n)
            if n < 2:
                return
            is_prime = [True]*(n+1)
            for i in range(2, len(is_prime)):
                if not is_prime[i]:
                    continue
                for j in range(i+i, len(is_prime), i):
                    is_prime[j] = False
                    if j in lookup:  # modified
                        uf.union_set(i-1, j-1)

        max_num = max(nums)
        uf = UnionFind(max_num)
        modified_sieve_of_eratosthenes(max_num, set(nums), uf)
        return all(uf.find_set(a-1) == uf.find_set(b-1) for a, b in zip(nums, sorted(nums)))
