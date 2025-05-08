# Time:  set: O(1)
#        get: O(logn)

import collections
import bisect


class TimeMap(object):

    def __init__(self):
        
        self.lookup = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        
        self.lookup[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        
        A = self.lookup.get(key, None)
        if A is None:
            return ""
        i = bisect.bisect_right(A, (timestamp+1, 0))
        return A[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
