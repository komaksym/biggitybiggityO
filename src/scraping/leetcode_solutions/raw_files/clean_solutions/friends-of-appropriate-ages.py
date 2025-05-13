# Time:  O(a^2 + n), a is the number of ages,
#                    n is the number of people

import collections


class Solution(object):
    def numFriendRequests(self, ages):
        def request(a, b):
            return 0.5*a+7 < b <= a

        c = collections.Counter(ages)
        return sum(int(request(a, b)) * c[a]*(c[b]-int(a == b))
                   for a in c
                   for b in c)

