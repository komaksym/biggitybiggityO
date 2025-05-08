# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        maximumHeight.sort()
        result, prev = 0, maximumHeight[-1]+1
        for x in reversed(maximumHeight):
            prev = min(x, prev-1)
            if prev == 0:
                return -1
            result += prev
        return result
