# Time:  O(n * m^2)

import collections


class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        
        language_sets = list(map(set, languages))          candidates = set(i-1 for u, v in friendships if not language_sets[u-1] & language_sets[v-1] for i in [u, v]) 
        for i in candidates: 
            count += collections.Counter(languages[i])
        return len(candidates) - max(list(count.values()) + [0])
