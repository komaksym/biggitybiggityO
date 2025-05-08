# Time:  O(m * 2^m + 3^m + 2^(3 * m) * logn) = O(2^(3 * m) * logn)

import collections
import itertools
from functools import reduce


# better complexity for small m, super large n
# matrix exponentiation solution
class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def backtracking(mask1, mask2, basis, result):  # Time: O(2^m), Space: O(2^m)
            if not basis:
                result.append(mask2)
                return
            for i in range(3):
                if (mask1 == -1 or mask1//basis%3 != i) and (mask2 == -1 or mask2//(basis*3)%3 != i):
                    backtracking(mask1, mask2+i*basis if mask2 != -1 else i*basis, basis//3, result)

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b % MOD for a, b in zip(row, col)) % MOD for col in ZB] for row in A]
 
        def matrix_expo(A, K):
            result = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def normalize(basis, mask):
            norm = {}
            result = 0
            while basis:
                x = mask//basis%3
                if x not in norm:
                    norm[x] = len(norm)
                result += norm[x]*basis
                basis //= 3
            return result

        if m > n:
            m, n = n, m
        basis = 3**(m-1)
        masks = []
        backtracking(-1, -1, basis, masks)  # Time: O(2^m), Space: O(2^m)
        assert(len(masks) == 3 * 2**(m-1))
        lookup = {mask:normalize(basis, mask) for mask in masks}  # Time: O(m * 2^m)
        normalized_mask_cnt = collections.Counter(lookup[mask] for mask in masks)
        assert(len(normalized_mask_cnt) == 3*2**(m-1) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
        adj = collections.defaultdict(list)
        for mask in normalized_mask_cnt.keys():  # O(3^m) leaves which are all in depth m => Time: O(3^m), Space: O(3^m)
            backtracking(mask, -1, basis, adj[mask])
        normalized_adj = collections.defaultdict(lambda:collections.defaultdict(int))
        for mask1, masks2 in adj.items():
            for mask2 in masks2:
                normalized_adj[mask1][lookup[mask2]] = (normalized_adj[mask1][lookup[mask2]]+1)%MOD
        assert(2*3**m // 3 // 2 // 3 <= sum(len(v) for v in normalized_adj.values()) <= 2*3**m // 3 // 2)
        return reduce(lambda x,y: (x+y)%MOD,
                      matrix_mult([list(normalized_mask_cnt.values())],
                                   matrix_expo([[normalized_adj[mask1][mask2]
                                                 for mask2 in normalized_mask_cnt.keys()] 
                                                 for mask1 in normalized_mask_cnt.keys()], n-1))[0],
                      0)  # Time: O((2^m)^3 * logn), Space: O((2^m)^2)


# Time:  O(n * 3^m)
import collections


# better complexity for small m, large n
class Solution2(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def find_masks(m, basis):  # Time: 3 + 3*2 + 3*2*2 + ... + 3*2^(m-1) = 3 * (2^m - 1) = O(2^m), Space: O(2^m)
            masks = [0]
            for c in range(m):
                new_masks = []
                for mask in masks:
                    choices = {0, 1, 2}
                    if c > 0:
                        choices.discard(mask//basis)  # get left grid
                    for x in choices:
                        new_masks.append((x*basis)+(mask//3))  # encoding mask
                masks = new_masks
            return masks

        def find_adj(m, basis, dp):
            adj = collections.defaultdict(list)
            for mask in dp.keys():  # O(2^m)
                adj[mask].append(mask)
            for c in range(m):
                assert(sum(len(v) for v in adj.values()) == (3**c * 2**(m-(c-1)) if c >= 1 else 3 * 2**(m-1)) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
                new_adj = collections.defaultdict(list)
                for mask1, mask2s in adj.items():
                    for mask in mask2s:
                        choices = {0, 1, 2}
                        choices.discard(mask%3)  # get up grid
                        if c > 0:
                            choices.discard(mask//basis)  # get left grid
                        for x in choices:
                            new_adj[mask1].append((x*basis)+(mask//3))  # encoding mask
                adj = new_adj
            assert(sum(3**c * 2**(m-(c-1)) if c >= 1 else 3 * 2**(m-1) for c in range(m)) == 4*3**m-9*2**(m-1))
            return adj
 
        def normalize(basis, mask):
            norm = {}
            result = 0
            while basis:
                x = mask//basis%3
                if x not in norm:
                    norm[x] = len(norm)
                result += norm[x]*basis
                basis //= 3
            return result

        if m > n:
            m, n = n, m
        basis = 3**(m-1)
        masks = find_masks(m, basis)  # alternative of backtracking, Time: O(2^m), Space: O(2^m)
        assert(len(masks) == 3 * 2**(m-1))
        lookup = {mask:normalize(basis, mask) for mask in masks}  # Time: O(m * 2^m)
        dp = collections.Counter(lookup[mask] for mask in masks)  # normalize colors to speed up performance
        adj = find_adj(m, basis, dp)  # alternative of backtracking, Time: O(3^m), Space: O(3^m)
        normalized_adj = collections.defaultdict(lambda:collections.defaultdict(int))
        for mask1, mask2s in adj.items():
            for mask2 in mask2s:
                normalized_adj[lookup[mask1]][lookup[mask2]] = (normalized_adj[lookup[mask1]][lookup[mask2]]+1)%MOD
        assert(2*3**m // 3 // 2 // 3 <= sum(len(v) for v in normalized_adj.values()) <= 2*3**m // 3 // 2)
        for _ in range(n-1):  # Time: O(n * 3^m), Space: O(2^m)
            assert(len(dp) == 3*2**(m-1) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            new_dp = collections.Counter()
            for mask, v in dp.items():
                for new_mask, cnt in normalized_adj[mask].items():
                    new_dp[lookup[new_mask]] = (new_dp[lookup[new_mask]] + v*cnt) % MOD
            dp = new_dp
        return reduce(lambda x,y: (x+y)%MOD, iter(dp.values()), 0)  # Time: O(2^m)


# Time:  (m * n grids) * (O(3*3*2^(m-2)) possible states per grid) = O(n * m * 2^m)
import collections


# better complexity for large m, large n
class Solution3(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def normalize(basis, mask, lookup):  # compute and cache, at most O(3*2^(m-3)) time and space
            if mask not in lookup[basis]:
                norm = {}
                result, b = 0, basis
                while b:
                    x = mask//b%3
                    if x not in norm:
                        norm[x] = len(norm)
                    result += norm[x]*b
                    b //= 3
                lookup[basis][mask] = result
            return lookup[basis][mask]

        if m > n:
            m, n = n, m
        basis = b = 3**(m-1)
        lookup = collections.defaultdict(dict)
        dp = collections.Counter({0: 1})
        for idx in range(m*n):
            r, c = divmod(idx, m)
            assert(r != 0 or c != 0 or len(dp) == 1)
            assert(r != 0 or c == 0 or len(dp) == 3*2**(c-1) // 3 // (2 if c >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            assert(r == 0 or c != 0 or len(dp) == 3*2**(m-1) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            assert(r == 0 or c == 0 or len(dp) == (1 if m == 1 else 2 if m == 2 else 3*3 * 2**(m-2) // 3 // 2))  # divided by 3 * 2 for m >= 3 is since the first two colors of window are normalized to speed up performance
            new_dp = collections.Counter()
            for mask, v in dp.items():
                choices = {0, 1, 2}
                if r > 0:
                    choices.discard(mask%3)  # get up grid
                if c > 0:
                    choices.discard(mask//basis)  # get left grid
                for x in choices:
                    new_mask = normalize(basis//b, ((x*basis)+(mask//3))//b, lookup)*b  # encoding mask
                    new_dp[new_mask] = (new_dp[new_mask]+v)%MOD
            if b > 1:
                b //= 3
            dp = new_dp
        return reduce(lambda x,y: (x+y)%MOD, iter(dp.values()), 0)  # Time: O(2^m)
