from functools import reduce
# Time:  O(n)

# bottom-up solution
class Solution(object):
    def findTheWinner(self, n, k):
        return reduce(lambda idx, n:(idx+k)%(n+1), range(1, n), 0)+1


# Time:  O(n)
# top-down solution
class Solution2(object):
    def findTheWinner(self, n, k):
        def f(idx, n, k):
            if n == 1:
                return 0
            return (k+f((idx+k)%n, n-1, k))%n
        
        return f(0, n, k)+1
