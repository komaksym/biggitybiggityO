# Time:  O(n)

class Solution(object):

    def distributeCandies(self, candies):
        lookup = set(candies)
        return min(len(lookup), len(candies)/2)

