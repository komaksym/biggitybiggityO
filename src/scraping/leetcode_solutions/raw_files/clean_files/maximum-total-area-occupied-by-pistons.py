# Time:  O(h)

import itertools


# line sweep, difference array
class Solution(object):
    def maxArea(self, height, positions, directions):
        diff = [0]*(2*height+1)
        for d, i in zip(directions, positions):
            if d == 'U':
                diff[height-i] -= 1
                diff[(height-i)+height] += 1
            else:
                diff[i] += 1
                diff[i+height] -= 1
        result = total = sum(positions)
        cnt = directions.count('U')
        for t in range(1, len(diff)):
            total += -(len(directions)-cnt)+cnt
            result = max(result, total)
            cnt += diff[t]
        return result


# Time:  O(nlogn)
import collections
import itertools


# sort, line sweep, difference array
class Solution2(object):
    def maxArea(self, height, positions, directions):
        diff = collections.defaultdict(int)
        for d, i in zip(directions, positions):
            if d == 'U':
                diff[height-i] -= 1
                diff[(height-i)+height] += 1
            else:
                diff[i] += 1
                diff[i+height] -= 1
        result = total = sum(positions)
        cnt = directions.count('U')
        prev = 0
        for t, d in sorted(diff.items()):
            total += (t-prev)*(-(len(directions)-cnt)+cnt)
            result = max(result, total)
            cnt += d
            prev = t
        return result
