# Time:  O(1)

# math
class Solution(object):
    def differenceOfSums(self, n, m):
        
        def arithmetic_progression_sum(a, d, l):
            return (a+(a+(l-1)*d))*l//2
    
        return arithmetic_progression_sum(1, 1, n) - 2*arithmetic_progression_sum(m, m, n//m)


# Time:  O(1)
# math
class Solution2(object):
    def differenceOfSums(self, n, m):
        
        return (n+1)*n//2 - 2*(((n//m+1)*(n//m)//2)*m)
