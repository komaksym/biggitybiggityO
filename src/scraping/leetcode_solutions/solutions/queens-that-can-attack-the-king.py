# Time:  O(1)

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        dirctions = [(-1, 0), (0, 1), (1, 0), (0, -1),
                     (-1, 1), (1, 1), (1, -1), (-1, -1)]
        result = []
        lookup = {(i, j) for i, j in queens}
        for dx, dy in dirctions:
            for i in range(1, 8):
                x, y = king[0] + dx*i, king[1] + dy*i
                if (x, y) in lookup:
                    result.append([x, y])
                    break
        return result
