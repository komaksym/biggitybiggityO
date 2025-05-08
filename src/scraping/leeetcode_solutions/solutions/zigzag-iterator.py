# Time:  O(n)

import collections


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def __next__(self):
        
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        
        return bool(self.q)


