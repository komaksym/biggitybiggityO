# Time:  O(n)

# hash table
class Solution(object):
    def minimizedStringLength(self, s):
        return len(set(s))
