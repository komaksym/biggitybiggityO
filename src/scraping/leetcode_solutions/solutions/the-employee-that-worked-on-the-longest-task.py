# Time:  O(l)

# array
class Solution(object):
    def hardestWorker(self, n, logs):
        return logs[max(range(len(logs)), key=lambda x: (logs[x][1]-(logs[x-1][1] if x-1 >= 0 else 0), -logs[x][0]))][0]
