# Time:  O(n * k), n = len(s), k = len(sub)

import collections


# brute force
class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        def transform(x):
            return ord(x)-ord('0') if x.isdigit() else ord(x)-ord('a')+10 if x.islower() else ord(x)-ord('A')+36

        def check(i):
            return all(sub[j] == s[i+j] or lookup[sub[j]][s[i+j]] for j in range(len(sub)))
            
        lookup = [[0]*62 for _ in range(62)]
        for a, b in mappings:
            lookup[transform(a)][transform(b)] = 1
        s = list(map(transform, s))
        sub = list(map(transform, sub))
        return any(check(i) for i in range(len(s)-len(sub)+1))


# Time:  O(n * k), n = len(s), k = len(sub)
import collections


# brute force
class Solution2(object):
    def matchReplacement(self, s, sub, mappings):
        def check(i):
            return all(sub[j] == s[i+j] or (sub[j], s[i+j]) in lookup for j in range(len(sub)))
            
        lookup = set()
        for a, b in mappings:
            lookup.add((a, b))
        return any(check(i) for i in range(len(s)-len(sub)+1))
