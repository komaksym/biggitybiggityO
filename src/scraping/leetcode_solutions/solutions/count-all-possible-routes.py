# Time:  O(nlogn + n * f)
# Space: O(n * f)

import bisect
from functools import reduce


class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9+7

        s, f = locations[start], locations[finish]
        locations.sort()
        start, finish = bisect.bisect_left(locations, s), bisect.bisect_left(locations, f)

        left = [[0]*(fuel+1) for _ in range(len(locations))] 
        right = [[0]*(fuel+1) for _ in range(len(locations))] 
        for f in range(1, fuel+1):
            for j in range(len(locations)-1):
                d = locations[j+1]-locations[j]
                if f > d:
                    left[j][f] = (right[j+1][f-d] + 2*left[j+1][f-d] % MOD) % MOD
                elif f == d:
                    left[j][f] = int(j+1 == start)
            for j in range(1, len(locations)):
                d = locations[j]-locations[j-1]
                if f > d:
                    right[j][f] = (left[j-1][f-d] + 2*right[j-1][f-d] % MOD) % MOD
                elif f == d:
                    right[j][f] = int(j-1 == start)
        result = int(start == finish)
        for f in range(1, fuel+1):
            result = ((result + left[finish][f]) % MOD + right[finish][f]) % MOD
        return result


# Time:  O(n^2 * f)
# Space: O(n * f)
class Solution2(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0]*(fuel+1) for _ in range(len(locations))]
        dp[start][0] = 1
        for f in range(fuel+1):
            for i in range(len(locations)):
                for j in range(len(locations)):
                    if i == j:
                        continue
                    d = abs(locations[i]-locations[j])
                    if f-d < 0:
                        continue
                    dp[i][f] = (dp[i][f]+dp[j][f-d])%MOD
        return reduce(lambda x, y: (x+y)%MOD, dp[finish])
