# Time:  O(1)

class Solution(object):
    def squareIsWhite(self, coordinates):
        return (ord(coordinates[0])-ord('a'))%2 != (ord(coordinates[1])-ord('1'))%2
