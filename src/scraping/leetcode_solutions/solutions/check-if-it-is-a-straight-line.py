# Time:  O(n)

class Solution(object):
    def checkStraightLine(self, coordinates):
        i, j = coordinates[:2]
        return all(i[0] * j[1] - j[0] * i[1] +
                   j[0] * k[1] - k[0] * j[1] +
                   k[0] * i[1] - i[0] * k[1] == 0
                   for k in coordinates)
