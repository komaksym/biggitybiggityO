# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort()
        for i, c in enumerate(capacity):
            if c > additionalRocks:
                return i
            additionalRocks -= c
        return len(capacity)
