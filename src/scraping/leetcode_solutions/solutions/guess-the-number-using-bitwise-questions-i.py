from functools import reduce
# Time:  O(logn):

# bit manipulation
class Solution(object):
    def findNumber(self):
        
        return reduce(lambda accu, x: accu|x, (1<<i for i in range(30) if commonSetBits(1<<i)))
