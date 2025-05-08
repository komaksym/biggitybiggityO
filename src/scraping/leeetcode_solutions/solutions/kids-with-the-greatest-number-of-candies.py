# Time:  O(n)

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        max_num = max(candies)
        return [x + extraCandies >= max_num for x in candies]
