# Time:  O(1)

import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        self.__radius = radius
        self.__x_center = x_center
        self.__y_center = y_center
        

    def randPoint(self):
        r = (self.__radius) * math.sqrt(random.uniform(0, 1))
        theta = (2*math.pi) * random.uniform(0, 1)
        return (r*math.cos(theta) + self.__x_center,
                r*math.sin(theta) + self.__y_center)



