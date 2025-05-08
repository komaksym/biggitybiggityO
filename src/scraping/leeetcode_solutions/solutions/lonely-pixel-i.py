# Time:  O(m * n)

class Solution(object):
    def findLonelyPixel(self, picture):
        
        rows, cols = [0] * len(picture),  [0] * len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        result = 0
        for i in range(len(picture)):
            if rows[i] == 1:
                for j in range(len(picture[0])):
                     result += picture[i][j] == 'B' and cols[j] == 1
        return result


class Solution2(object):
    def findLonelyPixel(self, picture):
        
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') \
               for col in zip(*picture))

