# Time:  O(n)

class Solution(object):
    def removeVowels(self, S):
        lookup = set("aeiou")
        return "".join(c for c in S if c not in lookup)
