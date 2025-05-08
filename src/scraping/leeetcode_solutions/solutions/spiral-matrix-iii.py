# Time:  O(max(m, n)^2)

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        
        r, c = r0, c0
        result = [[r, c]]
        x, y, n, i = 0, 1, 0, 0
        while len(result) < R*C:
            r, c, i = r+x, c+y, i+1
            if 0 <= r < R and 0 <= c < C:
                result.append([r, c])
            if i == n//2+1:
                x, y, n, i = y, -x, n+1, 0
        return result

