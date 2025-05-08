# Time:  ctor:  O(n + p^2), n is the total size of patterns
#                         , p is the number of patterns
#        query: O(m + z), m is the total size of query string
#                       , z is the number of all matched strings 
#                       , query time would be O(m) if we don't use all the matched patterns
#                  , 
# Aho–Corasick automata
# reference:
# - http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Small02.pdf
# - http://algo.pw/algo/64/python

import collections


class AhoNode(object):
    def __init__(self):
        self.children = collections.defaultdict(AhoNode)
        self.suffix = None
        self.outputs = []


class AhoTrie(object):

    def step(self, letter):
        while self.__node and letter not in self.__node.children:
            self.__node = self.__node.suffix
        self.__node = self.__node.children[letter] if self.__node else self.__root
        return self.__node.outputs 
    
    def __init__(self, patterns):
        self.__root = self.__create_ac_trie(patterns)
        self.__node = self.__create_ac_suffix_and_output_links(self.__root)
    
    def __create_ac_trie(self, patterns): 
        for i, pattern in enumerate(patterns):
            node = root
            for c in pattern:
                node = node.children[c]
            node.outputs.append(i)
        return root

    def __create_ac_suffix_and_output_links(self, root): 
        for node in root.children.values():
            queue.append(node)
            node.suffix = root

        while queue:
            node = queue.popleft()
            for c, child in node.children.items():
                queue.append(child)
                suffix = node.suffix
                while suffix and c not in suffix.children:
                    suffix = suffix.suffix
                child.suffix = suffix.children[c] if suffix else root
                child.outputs += child.suffix.outputs 
        
        return root


class StreamChecker(object):

    def __init__(self, words):
        
        self.__trie = AhoTrie(words)

    def query(self, letter): 
        
        return len(self.__trie.step(letter)) > 0
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
