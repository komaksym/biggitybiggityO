# Time:  O(n)

import itertools


class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        total = sum(itertools.islice(calories, 0, k))
        result = int(total > upper)-int(total < lower)
        for i in range(k, len(calories)):
            total += calories[i]-calories[i-k]
            result += int(total > upper)-int(total < lower)
        return result
