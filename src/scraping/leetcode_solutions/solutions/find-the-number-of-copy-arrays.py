# Time:  O(n)

# greedy
class Solution(object):
    def countArrays(self, original, bounds):
        left, right = bounds[0]
        result = right-left+1
        for i in range(1, len(original)):
            diff = original[i]-original[i-1]
            left = max(left+diff, bounds[i][0])
            right = min(right+diff, bounds[i][1])
            result = min(result, max(right-left+1, 0))
        return result
