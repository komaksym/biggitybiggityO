# Time:  O(n)

class Solution(object):
    def mergeTriplets(self, triplets, target):
        result = [0]*3
        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                result = [max(result[i], t[i]) for i in range(3)]
        return result == target
