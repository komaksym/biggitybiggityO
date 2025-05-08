# Time:  O(n)

# hash table
class Solution(object):
    def repeatedCharacter(self, s):
        
        lookup = set()
        for c in s:
            if c in lookup:
                break
            lookup.add(c)
        return c
