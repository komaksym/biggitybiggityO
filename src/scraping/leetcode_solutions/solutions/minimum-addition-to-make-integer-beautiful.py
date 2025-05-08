# Time:  O(logn)

# greedy
class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        total, m = 0, n
        while m:
            total += m%10
            m //= 10
        m, l = n, 0
        while total > target:
            while True:
                total -= m%10
                m //= 10
                l += 1
                if m%10 != 9:
                    break
            total += 1
            m += 1
        return m*10**l-n
