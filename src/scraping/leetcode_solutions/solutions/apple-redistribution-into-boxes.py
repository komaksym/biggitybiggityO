# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def minimumBoxes(self, apple, capacity):
        capacity.sort(reverse=True)
        total = sum(apple)
        for i in range(len(capacity)):
            total -= capacity[i]
            if total <= 0:
                return i+1
        return -1
