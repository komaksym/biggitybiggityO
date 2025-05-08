# Time:  ctor:         O(1)
#        insert:       O(n)
#        count_word:   O(n)
#        count_prefix: O(n)
#        erase:        O(n)

class Node:
    def __init__(self):
        self.children = [None]*26
        self.pcnt = 0
        self.cnt = 0

class Trie(object):

    def __init__(self):
        self.__trie = Node()

    def insert(self, word):
        
        curr = self.__trie
        curr.pcnt += 1
        for c in word:
            if curr.children[ord(c)-ord('a')] is None:
                curr.children[ord(c)-ord('a')] = Node()
            curr = curr.children[ord(c)-ord('a')]
            curr.pcnt += 1
        curr.cnt += 1

    def countWordsEqualTo(self, word):
        
        curr = self.__trie
        for c in word:
            if curr.children[ord(c)-ord('a')] is None:
                return 0
            curr = curr.children[ord(c)-ord('a')]
        return curr.cnt

    def countWordsStartingWith(self, prefix):
        
        curr = self.__trie
        for c in prefix:
            if curr.children[ord(c)-ord('a')] is None:
                return 0
            curr = curr.children[ord(c)-ord('a')]
        return curr.pcnt

    def erase(self, word):
        
        cnt = self.countWordsEqualTo(word)
        if not cnt:
            return
        curr = self.__trie
        curr.pcnt -= 1
        for c in word:
            if curr.children[ord(c)-ord('a')].pcnt == 1:
                curr.children[ord(c)-ord('a')] = None 
                return
            curr = curr.children[ord(c)-ord('a')]
            curr.pcnt -= 1
        curr.cnt -= 1
