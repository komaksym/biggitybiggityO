# Time:  O(n * l)

import collections


# trie
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result = 0
        for w in words:
            curr = trie
            for i in range(len(w)):
                curr = curr[w[i], w[~i]]
                result += curr["_cnt"] if "_cnt" in curr else 0
            curr["_cnt"] = curr["_cnt"]+1 if "_cnt" in curr else 1
        return result
