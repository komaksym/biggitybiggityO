# Time:  O(n^2)

class Solution(object):
    def countDistinct(self, s):
        count = 0
        trie = {}
        for i in range(len(s)):
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr:
                    count += 1
                    curr[s[j]] = {}
                curr = curr[s[j]]
        return count
