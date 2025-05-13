# Time:  O(n), n is the length of the word

import collections


class Solution(object):

    def __init__(self):
        _trie = lambda: collections.defaultdict(_trie)
        self.trie = _trie()


    def buildDict(self, dictionary):
        for word in dictionary:
            reduce(dict.__getitem__, word, self.trie).setdefault("_end")


    def search(self, word):
        def find(word, curr, i, mistakeAllowed):
            if i == len(word):
                return "_end" in curr and not mistakeAllowed

            if word[i] not in curr:
                return any(find(word, curr[c], i+1, False) for c in curr if c != "_end") \
                           if mistakeAllowed else False

            if mistakeAllowed:
                return find(word, curr[word[i]], i+1, True) or \
                       any(find(word, curr[c], i+1, False) \
                           for c in curr if c not in ("_end", word[i]))
            return find(word, curr[word[i]], i+1, False)

        return find(word, self.trie, 0, True)




