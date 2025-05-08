# Time:  O(n)

from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        
        self.lookup = defaultdict(int)



    def add(self, number):
        
        self.lookup[number] += 1


    def find(self, value):
        
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (num != key or self.lookup[key] > 1):
                return True
        return False


