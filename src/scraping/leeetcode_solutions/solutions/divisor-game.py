# Time:  O(1)

# math
class Solution(object):
    def divisorGame(self, n):
        
       
       
       
       
       
       
       
        return n % 2 == 0


# Time:  O(nlogn)
# dp, number theory
class Solution2(object):
    def divisorGame(self, n):
        
        def factors(n):
            result = [[] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(i, n+1, i):
                    result[j].append(i)
            return result

        FACTORS = factors(n)
        dp = [False]*(n+1)
        for i in range(2, n+1):
            dp[i] = any(not dp[i-j] for j in FACTORS[i] if j != i)
        return dp[-1]


# Time:  O(nlogn)
# memoization, number theory
class Solution3(object):
    def divisorGame(self, n):
        
        def factors(n):
            result = [[] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(i, n+1, i):
                    result[j].append(i)
            return result
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in FACTORS[n] if i != n)
            return lookup[n]

        FACTORS = factors(n)
        lookup = [None]*(n+1)
        return memoization(n)


# Time:  O(n^(3/2))
# memoization
class Solution4(object):
    def divisorGame(self, n):
        
        def factors(n):
            for i in range(1, n+1):
                if i*i > n:
                    break
                if n%i:
                    continue
                yield i
                if n//i != i:
                    yield n//i
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in factors(n) if i != n)
            return lookup[n]

        lookup = [None]*(n+1)
        return memoization(n)


# Time:  O(n^2)
# memoization
class Solution5(object):
    def divisorGame(self, n):
        
        def factors(n):
            for i in range(1, n+1):
                if n%i:
                    continue
                yield i
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in factors(n) if i != n)
            return lookup[n]

        lookup = [None]*(n+1)
        return memoization(n)
