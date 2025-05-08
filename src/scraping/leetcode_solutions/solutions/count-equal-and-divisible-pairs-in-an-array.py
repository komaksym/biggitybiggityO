# Time:  O(nlogk + n * sqrt(k))

import collections


# math, number theory
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
    
        idxs = collections.defaultdict(list)
        for i, x in enumerate(nums):
            idxs[x].append(i)
        result = 0
        for idx in idxs.values():
            gcds = collections.Counter()
            for i in idx:
                gcd_i = gcd(i, k)
                result += sum(cnt for gcd_j, cnt in gcds.items() if gcd_i*gcd_j%k == 0)
                gcds[gcd_i] += 1
        return result


# Time:  O(nlogk + n * sqrt(k)^2) = O(n * k)
import collections


# math, number theory
class Solution2(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
    
        cnts = collections.defaultdict(collections.Counter)
        for i, x in enumerate(nums):
            cnts[x][gcd(i, k)] += 1
        result = 0
        for cnt in cnts.values():
            for x in cnt.keys():
                for y in cnt.keys():
                    if x > y or x*y%k:
                        continue
                    result += cnt[x]*cnt[y] if x != y else cnt[x]*(cnt[x]-1)//2
        return result


# Time:  O(n^2)
import collections


# brute force
class Solution3(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        idxs = collections.defaultdict(list)
        for i, x in enumerate(nums):
            idxs[x].append(i)
        return sum(idx[i]*idx[j]%k == 0 for idx in idxs.values() for i in range(len(idx)) for j in range(i+1, len(idx)))
