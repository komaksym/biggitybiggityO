# Time:  O(n * 2^n * (log(mx) + log(k * mn))) = O(n * 2^n * logk), mn = min(coins), mx = max(coins)

import itertools
from functools import reduce


# binary search, principle of inclusion and exclusion, number theory
class Solution(object):
    def findKthSmallest(self, coins, k):
        
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        def lcm(a, b):
            return a//gcd(a, b)*b
        
        def check(target):
            return sum((-1 if (i+1)&1 else +1)*(target//l) for i in range(1, len(coins)+1) for l in lookup[i]) >= k

        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        lookup = [[] for _ in range(len(coins)+1)]
        for i in range(1, len(coins)+1):
            for comb in itertools.combinations(coins, i):
                lookup[i].append(reduce(lcm, comb))
        mn = min(coins)
        l = 1
        for i in range(1, 25+1):
            l = lcm(l, i)
        return binary_search(mn, k*mn, check)


# Time:  O(n * 2^n * (log(mx) + log(k * mn))) = O(n * 2^n * logk), mn = min(coins), mx = max(coins)
# binary search, principle of inclusion and exclusion, number theory
class Solution2(object):
    def findKthSmallest(self, coins, k):
        
        def popcount(x):
            return bin(x).count('1')

        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        def lcm(a, b):
            return a//gcd(a, b)*b
    
        def check(target):
            return sum((-1 if (i+1)&1 else +1)*(target//l) for i in range(1, len(coins)+1) for l in lookup[i]) >= k

        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
    
        lookup = [[] for _ in range(len(coins)+1)]
        for mask in range(1, 1<<len(coins)):
            lookup[popcount(mask)].append(reduce(lcm, (coins[i] for i in range(len(coins)) if mask&(1<<i))))
        mn = min(coins)
        return binary_search(mn, k*mn, check)
