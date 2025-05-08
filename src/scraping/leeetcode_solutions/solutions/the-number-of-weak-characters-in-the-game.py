# Time:  O(nlogn)

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        
        properties.sort(cmp=lambda a, b: cmp(b[1], a[1]) if a[0] == b[0] else cmp(a[0], b[0]))
        result = max_d = 0
        for a, d in reversed(properties):
            if d < max_d:
                result += 1
            max_d = max(max_d, d)
        return result

    
# Time:  O(nlogn)
import collections


# faster in sort by using more class Solution(object):
    def numberOfWeakCharacters(self, properties):
        
        lookup = collections.defaultdict(list)
        for a, d in properties:
            lookup[a].append(d)
        result = max_d = 0
        for a in sorted(iter(lookup.keys()), reverse=True):
            result += sum(d < max_d for d in lookup[a])
            max_d = max(max_d, max(lookup[a]))
        return result
