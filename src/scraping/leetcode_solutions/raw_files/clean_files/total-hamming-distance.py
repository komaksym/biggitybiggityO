# Time:  O(n)

class Solution(object):
    def totalHammingDistance(self, nums):
        result = 0
        for i in range(32):
            counts = [0] * 2
            for num in nums:
                counts[(num >> i) & 1] += 1
            result += counts[0] * counts[1]
        return result


