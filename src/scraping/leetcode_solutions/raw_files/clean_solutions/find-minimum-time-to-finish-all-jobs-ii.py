# Time:  O(nlogn)

import itertools


# greedy
class Solution(object):
    def minimumTime(self, jobs, workers):
        def ceil_divide(a, b):
            return (a+(b-1))//b

        jobs.sort()
        workers.sort()
        return max(ceil_divide(j, w) for j, w in zip(jobs, workers))
