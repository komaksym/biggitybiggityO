# Time:  ctor: O(n * l), n is the number of products
#                      , l is the average length of product name
#        suggest: O(l^2)

import collections


class TrieNode(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(words, i)

    def add_info(self, words, i):
        self.infos.append(i)
        self.infos.sort(key=lambda x: words[x])
        if len(self.infos) > self.__TOP_COUNT:
            self.infos.pop()


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        
        trie = TrieNode()
        for i in range(len(products)):
            trie.insert(products, i)
        result = [[] for _ in range(len(searchWord))]
        for i, c in enumerate(searchWord):
            if c not in trie.leaves:
                break
            trie = trie.leaves[c]
            result[i] = [products[x] for x in trie.infos]
        return result


# Time:  ctor: O(n * l * log(n * l)), n is the number of products
#                                   , l is the average length of product name
#        suggest: O(l^2)
class TrieNode2(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode2)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(i)

    def add_info(self, i):
        if len(self.infos) == self.__TOP_COUNT:
            return
        self.infos.append(i)


class Solution2(object):
    def suggestedProducts(self, products, searchWord):
        
        products.sort()
        trie = TrieNode2()
        for i in range(len(products)):
            trie.insert(products, i)
        result = [[] for _ in range(len(searchWord))]
        for i, c in enumerate(searchWord):
            if c not in trie.leaves:
                break
            trie = trie.leaves[c]
            result[i] = [products[x] for x in trie.infos]
        return result


# Time:  ctor: O(n * l * log(n * l)), n is the number of products
#                                   , l is the average length of product name
#        suggest: O(l^2 * n)
import bisect


class Solution3(object):
    def suggestedProducts(self, products, searchWord):
        
        products.sort() 
        result = []
        prefix = ""
        for i, c in enumerate(searchWord): 
            prefix += c
            start = bisect.bisect_left(products, prefix) 
            new_products = []
            for j in range(start, len(products)): 
                if not (i < len(products[j]) and products[j][i] == c):
                    break
                new_products.append(products[j])
            products = new_products
            result.append(products[:3])
        return result
