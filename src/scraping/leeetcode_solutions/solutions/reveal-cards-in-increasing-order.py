# Time:  O(n)

import collections


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        
        d = collections.deque()
        deck.sort(reverse=True)
        for i in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(i)
        return list(d)
