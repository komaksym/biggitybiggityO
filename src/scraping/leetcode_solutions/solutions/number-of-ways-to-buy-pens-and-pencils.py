# Time:  O(min(t / c1, c2 / g)) = O(sqrt(t)), c1 = max(cost1, cost2)
#                                           , c2 = min(cost1, cost2)
#                                           ,  g = gcd(c1, c2)
# Space: O(1)

# math
class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        def ceil_divide(a, b):
            return (a+b-1)//b

        def arithmetic_progression_sum(a, d, l):
            return (a+(a+(l-1)*d))*l//2
            
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        lcm = cost1*cost2//gcd(cost1, cost2)
        result = 0
        d = lcm//cost2
        for i in range(min(total//cost1+1, lcm//cost1)):
            cnt = (total-i*cost1)//cost2+1
            l = ceil_divide(cnt, d)
            result += arithmetic_progression_sum(cnt, -d, l)
        return result


# Time:  O(t / c1), c1 = max(cost1, cost2)
#                 , c2 = min(cost1, cost2)
# Space: O(1)
# math
class Solution2(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        return sum((total-i*cost1)//cost2+1 for i in range(total//cost1+1))
