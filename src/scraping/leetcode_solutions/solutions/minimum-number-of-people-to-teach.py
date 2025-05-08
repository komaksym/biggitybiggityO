# Time:  O(n * m^2)
# Space: O(n * m)

import collections


class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        language_sets = list(map(set, languages)) 
        candidates = set(i-1 for u, v in friendships if not language_sets[u-1] & language_sets[v-1] for i in [u, v]) 
        count = collections.Counter()
        for i in candidates: 
            count += collections.Counter(languages[i])
        return len(candidates) - max(list(count.values()) + [0])
