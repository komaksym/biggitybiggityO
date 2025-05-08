# Time:  O(1)

# Chicken McNugget Theorem
class Solution(object):
    def mostExpensiveItem(self, primeOne, primeTwo):
        """
        :type primeOne: int
        :type primeTwo: int
        :rtype: int
        """
        return primeOne*primeTwo-primeOne-primeTwo


# Time:  O(p1 * p2)
# dp
class Solution2(object):
    def mostExpensiveItem(self, primeOne, primeTwo):
        """
        :type primeOne: int
        :type primeTwo: int
        :rtype: int
        """
        dp = [False]*max(primeOne, primeTwo)
        dp[0] = True
        result = 1
        for i in range(2, primeOne*primeTwo):
            dp[i%len(dp)] = dp[(i-primeOne)%len(dp)] or dp[(i-primeTwo)%len(dp)]
            if not dp[i%len(dp)]:
                result = i
        return result
