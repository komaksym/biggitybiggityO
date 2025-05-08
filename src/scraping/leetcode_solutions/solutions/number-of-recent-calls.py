# Time:  O(1) on average

import collections


class RecentCounter(object):

    def __init__(self):
        self.__q = collections.deque()

    def ping(self, t):
        
        self.__q.append(t)
        while self.__q[0] < t-3000:
            self.__q.popleft()
        return len(self.__q)
