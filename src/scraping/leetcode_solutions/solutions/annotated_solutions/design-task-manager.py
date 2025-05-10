# Time:  ctor:    O(tlogt)
#        add:     O(logt)
#        edit:    O(logt)
#        rmv:     O(logt)
#        execTop: O(logt)

from sortedcontainers import SortedList


# sorted list
class TaskManager(object):

    def __init__(self, tasks):
        self.__lookup = {}
        self.__sl = SortedList()
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.__sl.add((priority, taskId, userId))
        self.__lookup[taskId] = (userId, priority)

    def edit(self, taskId, newPriority):
        userId, _ = self.__lookup[taskId]
        self.rmv(taskId)
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId):
        userId, priority = self.__lookup.pop(taskId)
        self.__sl.remove((priority, taskId, userId))

    def execTop(self):
        if not self.__sl:
            return -1
        _, taskId, userId = self.__sl[-1]
        self.rmv(taskId)
        return userId
