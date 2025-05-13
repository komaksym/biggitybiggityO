# Time:  O(n^2)

# Definition for a category handler.
class CategoryHandler:
    def haveSameCategory(self, a, b):
        pass


# brute force
class Solution(object):
    def numberOfCategories(self, n, categoryHandler):
        return sum(all(not categoryHandler.haveSameCategory(j, i) for j in range(i)) for i in range(n))
