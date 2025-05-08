# Time:  O(n)


class Solution(object):
    def findSolution(self, customfunction, z):
        
        result = []
        x, y = 1, 1
        while customfunction.f(x, y) < z:
            y += 1
        while y > 0:
            while y > 0 and customfunction.f(x, y) > z:
                y -= 1
            if y > 0 and customfunction.f(x, y) == z:
                result.append([x, y])
            x += 1
        return result
