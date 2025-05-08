# Time:  O(n)

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
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
