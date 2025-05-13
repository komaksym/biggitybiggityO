# Time:  ctor: O(n)
#        dot_product: O(min(n, m))

class Solution:
    def __init__(self, nums):
        self.lookup = {i:v for i, v in enumerate(nums) if v}

    def dotProduct(self, vec):
        if len(self.lookup) > len(vec.lookup):
            self, vec = vec, self
        return sum(v*vec.lookup[i] for i, v in self.lookup.items() if i in vec.lookup)
