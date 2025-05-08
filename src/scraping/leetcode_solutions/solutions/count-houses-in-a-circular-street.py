# Time:  O(k)

# Definition for a street.
class Street:
    def openDoor(self):
        pass
    def closeDoor(self):
        pass
    def isDoorOpen(self):
        pass
    def moveRight(self):
        pass
    def moveLeft(self):
        pass


# constructive algorithms
class Solution(object):
    def houseCount(self, street, k):
        
        for _ in range(k):
            street.closeDoor()
            street.moveRight()
        for result in range(k+1):
            if street.isDoorOpen():
                break
            street.openDoor()
            street.moveRight()
        return result
