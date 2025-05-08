# Time:  O(n^4)

class Solution(object):
    def splitArraySameAverage(self, A):
        
        def possible(total, n):
            for i in range(1, n//2+1):
                if total*i%n == 0:
                    return True
            return False
        n, s = len(A), sum(A)
        if not possible(n, s):
            return False

        sums = [set() for _ in range(n//2+1)]
        sums[0].add(0)
        for num in A: 
            for i in reversed(range(1, n//2+1)): 
                for prev in sums[i-1]: 
                    sums[i].add(prev+num)
        for i in range(1, n//2+1):
            if s*i%n == 0 and s*i//n in sums[i]:
                return True
        return False

