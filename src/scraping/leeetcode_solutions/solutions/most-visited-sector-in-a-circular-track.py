# Time:  O(n)
# Space: O(1)

class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        return list(range(rounds[0], rounds[-1]+1)) or \
               list(range(1, rounds[-1]+1)) + list(range(rounds[0], n+1))
