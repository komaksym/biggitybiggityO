# Time:  ctor:         O(nlogn)
#        changeRating: O(logn)
#        highestRated: O(1)

import collections
import itertools
from sortedcontainers import SortedList


# sorted list
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.__food_to_cuisine = {}
        self.__food_to_rating = {}
        self.__cusine_to_rating_foods = collections.defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.__food_to_cuisine[food] = cuisine
            self.__food_to_rating[food] = rating
            self.__cusine_to_rating_foods[cuisine].add((-rating, food))

    def changeRating(self, food, newRating):
        old_rating = self.__food_to_rating[food]
        cuisine = self.__food_to_cuisine[food]
        self.__cusine_to_rating_foods[cuisine].remove((-old_rating, food))
        self.__food_to_rating[food] = newRating
        self.__cusine_to_rating_foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine):
        return self.__cusine_to_rating_foods[cuisine][0][1]
