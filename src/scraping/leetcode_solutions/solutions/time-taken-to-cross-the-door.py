# Time:  O(n)

import collections
import itertools


# queue, simulation
class Solution(object):
    def timeTaken(self, arrival, state):
        
        def go_until(t):
            while curr[0] <= t and any(q):
                if not q[direction[0]]:
                    direction[0] ^= 1
                result[q[direction[0]].popleft()] = curr[0]
                curr[0] += 1
    
        UNKNOWN, ENTERING, EXITING = list(range(-1, 1+1))
        result = [0]*len(arrival)
        curr, direction = [float("-inf")], [UNKNOWN]
        q = [collections.deque(), collections.deque()]
        for i, (a, s) in enumerate(zip(arrival, state)):
            go_until(a-1)
            q[s].append(i)
            if not (a <= curr[0]):
                curr, direction = [a], [EXITING]
        go_until(float("inf"))
        return result
