# Time:  O(logn)

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def check(A, B, N, lcm, target):
            return target//A + target//B - target//lcm >= N

        lcm = A*B // gcd(A, B)
        left, right = min(A, B), max(A, B)*N
        while left <= right:
            mid = left + (right-left)//2
            if check(A, B, N, lcm, mid):
                right = mid-1
            else:
                left = mid+1
        return left % (10**9 + 7)

