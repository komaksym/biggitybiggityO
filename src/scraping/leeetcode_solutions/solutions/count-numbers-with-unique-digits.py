# Time:  O(n)

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        
        if n == 0:
            return 1
        result = cnt = 1
        for i in range(n-1):
            cnt *= 9-i
            result += cnt
        return 1+9*result


# Time:  O(n)
class Solution2(object):
    def countNumbersWithUniqueDigits(self, n):
        
        fact = [1]*2
        def nPr(n, k):
            while len(fact) <= n: 
                fact.append(fact[-1]*len(fact))
            return fact[n]//fact[n-k]

        return 1+9*sum(nPr(9, i) for i in range(n))
