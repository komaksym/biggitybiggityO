# Time:  O(n^2)

class Solution(object):
    def maximalRectangle(self, matrix):
        
        def largestRectangleArea(heights):
            stk, result, i = [-1], 0, 0
            for i in range(len(heights)+1):
                while stk[-1] != -1 and (i == len(heights) or heights[stk[-1]] >= heights[i]):
                    result = max(result, heights[stk.pop()]*((i-1)-stk[-1]))
                stk.append(i) 
            return result

        if not matrix:
            return 0
        result = 0
        heights = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            result = max(result, largestRectangleArea(heights))
        return result


# Time:  O(n^2)
# DP solution.
class Solution2(object):
    def maximalRectangle(self, matrix):
        
        if not matrix:
            return 0

        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0 for _ in range(n)]
        H = [0 for _ in range(n)]
        R = [n for _ in range(n)]

        for i in range(m):
            left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1

            right = n
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j

        return result

