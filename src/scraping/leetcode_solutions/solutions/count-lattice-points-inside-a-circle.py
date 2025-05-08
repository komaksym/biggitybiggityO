# Time:  O(n * r^2)

# math, hash table
class Solution(object):
    def countLatticePoints(self, circles):
        
        lookup = set()
        for x, y, r in circles:
            for i in range(-r, r+1):
                for j in range(-r, r+1):
                    if i**2+j**2 <= r**2:
                        lookup.add(((x+i), (y+j)))
        return len(lookup)


# Time:  O(n * max_x * max_y)
# math
class Solution2(object):
    def countLatticePoints(self, circles):
        
        max_x = max(x+r for x, _, r in circles)
        max_y = max(y+r for _, y, r in circles)
        result = 0
        for i in range(max_x+1):
            for j in range(max_y+1):
                if any((i-x)**2+(j-y)**2 <= r**2 for x, y, r in circles):
                    result += 1
        return result
