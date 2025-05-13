# Time:  O(n)

import threading


class Solution(object):
    
    def __init__(self):
        self.__l = threading.Lock()
        self.__light = 1

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        with self.__l:
            if self.__light != roadId:
                self.__light = roadId
                turnGreen()
            crossCar()
