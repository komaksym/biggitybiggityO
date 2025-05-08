from functools import reduce
# Time:  O(1)

# math
class Solution(object):
    def numberOfWays(self, n):
        
        MOD = 10**9+7
  
       
       

       
       
       
       
       

       
       
       
       

       
       
       
       
       
       
       

       
       
       
       
       
       

       
       
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       

       
        return (1+((n//2)+1)*(n//2)//2)%MOD


# Time:  O(1)
# math
class Solution2(object):
    def numberOfWays(self, n):
        
        MOD = 10**9+7
        def count_1_2_6(n):
           
           
            return (n//2+1)*((n//6)-0+1)-3*((n//6)+0)*((n//6)-0+1)//2

        return reduce(lambda x, y: (x+count_1_2_6(n-4*y))%MOD, (i for i in range(min(n//4, 2)+1)), 0)


# Time:  O(n)
# math
class Solution3(object):
    def numberOfWays(self, n):
        
        MOD = 10**9+7
        def count_1_2(n):
            return n//2+1
    
        def count_1_2_6(n):
            return sum(count_1_2(n-6*i) for i in range((n//6)+1))

        return reduce(lambda x, y: (x+count_1_2_6(n-4*y))%MOD, (i for i in range(min(n//4, 2)+1)), 0)


# Time:  O(n)
# dp
class Solution4(object):
    def numberOfWays(self, n):
        
        MOD = 10**9+7
        dp = [0]*(n+1)
        dp[0] = 1
        for i in (1, 2, 6):
            for j in range(i, n+1):
                dp[j] += dp[j-i]
        return reduce(lambda x, y: (x+dp[n-4*y])%MOD, (i for i in range(min(n//4, 2)+1)), 0)
