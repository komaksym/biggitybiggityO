# Time:  ctor:   O(n), n is number of words in the dictionary.
#        lookup: O(1)

import collections


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        
        self.lookup_ = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.abbreviation(word)
            self.lookup_[abbr].add(word)


    def isUnique(self, word):
        
        abbr = self.abbreviation(word)
        return self.lookup_[abbr] <= {word}


    def abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]



