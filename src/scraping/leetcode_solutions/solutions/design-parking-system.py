# Time:  O(1)

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.__space = [0, big, medium, small]

    def addCar(self, carType):
        if self.__space[carType] > 0:
            self.__space[carType] -= 1
            return True
        return False
