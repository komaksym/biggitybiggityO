# Time:  O(n + m)

# hash table
class Solution(object):
    def reportSpam(self, message, bannedWords):
        THRESHOLD = 2
        lookup = set(bannedWords)
        return sum(m in lookup for m in message) >= THRESHOLD
