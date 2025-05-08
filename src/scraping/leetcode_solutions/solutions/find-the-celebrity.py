# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):  # noqa
                candidate = i        # All candidates < i are not celebrity candidates.
        for i in range(n):
            candidate_knows_i = knows(candidate, i) # noqa
            i_knows_candidate = knows(i, candidate) # noqa
            if i != candidate and (candidate_knows_i or
                                   not i_knows_candidate):
                return -1
        return candidate

