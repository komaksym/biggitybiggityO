# Time:  O(nlogn)

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        
        asteroids.sort()
        for x in asteroids:
            if x > mass:
                return False
            mass += min(x, asteroids[-1]-mass)
        return True
