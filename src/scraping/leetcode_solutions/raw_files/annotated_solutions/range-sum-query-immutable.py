# Time:  ctor:   O(n),
#        lookup: O(1)

class Solution(object):
    def __init__(self, nums):
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num),

    def sumRange(self, i, j):
        return self.accu[j + 1] - self.accu[i]



