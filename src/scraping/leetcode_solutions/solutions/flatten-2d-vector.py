# Time:  O(1)

from collections import deque


class Vector2D(object):

    def __init__(self, vec2d):
        self.stack = deque((len(v), iter(v)) for v in vec2d if v)

    def __next__(self):
        length, iterator = self.stack.popleft()
        if length > 1:
            self.stack.appendleft((length-1, iterator))
        return next(iterator)

    def hasNext(self):
        return bool(self.stack)
