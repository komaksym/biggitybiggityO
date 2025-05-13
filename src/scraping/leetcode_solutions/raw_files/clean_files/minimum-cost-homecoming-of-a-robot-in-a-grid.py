# Time:  O(m + n)

class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        [x0, y0], [x1, y1] = startPos, homePos
        return (sum(rowCosts[i] for i in range(min(x0, x1), max(x0, x1)+1))-rowCosts[x0]) + \
               (sum(colCosts[i] for i in range(min(y0, y1), max(y0, y1)+1))-colCosts[y0])
