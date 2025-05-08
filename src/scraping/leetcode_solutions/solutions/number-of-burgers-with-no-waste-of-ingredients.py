# Time:  O(1)

class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        return [tomatoSlices//2-cheeseSlices, 2*cheeseSlices - tomatoSlices//2] \
               if tomatoSlices%2 == 0 and 2*cheeseSlices <= tomatoSlices <= 4*cheeseSlices \
               else []
