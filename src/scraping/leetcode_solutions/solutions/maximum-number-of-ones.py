# Time:  O(1)

class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        
        if width < height:
            width, height = height, width

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       

        R, r = divmod(height, sideLength)
        C, c = divmod(width, sideLength)
        assert(R <= C)
        area_counts = [(r*c, (R+1)*(C+1)), \
                       (r*(sideLength-c), (R+1)*C), \
                       ((sideLength-r)*c, R*(C+1)), \
                       ((sideLength-r)*(sideLength-c), R*C)]
        result = 0
        for area, count in area_counts:
            area = min(maxOnes, area)
            result += count*area
            maxOnes -= area
            if not maxOnes:
                break
        return result
