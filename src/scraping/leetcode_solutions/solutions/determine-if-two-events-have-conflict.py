# Time:  O(1)

# array
class Solution(object):
    def haveConflict(self, event1, event2):
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])
