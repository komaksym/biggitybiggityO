# Time:  O(k)

# Definition for a street.
class Street:
    def closeDoor(self):
        pass
    def isDoorOpen(self):
        pass
    def moveRight(self):
        pass


# constructive algorithms
class Solution(object):
    def houseCount(self, street, k):
        
        while not street.isDoorOpen():
            street.moveRight()
        result = 0
        for i in range(k+1):
            if i and street.isDoorOpen():
                street.closeDoor()
                result = i
            street.moveRight()
        return result
