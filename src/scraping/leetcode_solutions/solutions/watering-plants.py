# Time:  O(n)

class Solution(object):
    def wateringPlants(self, plants, capacity):
        result, can = len(plants), capacity
        for i, x in enumerate(plants):
            if can < x:
                result += 2*i
                can = capacity
            can -= x
        return result
