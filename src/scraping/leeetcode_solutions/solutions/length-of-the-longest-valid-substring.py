# Time:  O((m + n) * l), n = len(word), m = len(forbidden), l = max(len(w) for w in forbidden)

import collections


# two pointers, sliding window, trie
class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for w in forbidden:
            reduce(dict.__getitem__, w, trie)["_end"]
        result = 0
        right = len(word)-1
        for left in reversed(range(len(word))):
            node = trie
            for i in range(left, right+1):
                if word[i] not in node: 
                    break
                node = node[word[i]]
                if "_end" in node:
                    right = i-1
                    break
            result = max(result, right-left+1)
        return result
