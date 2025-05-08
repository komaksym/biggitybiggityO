# Time:  O(nlogn)

# sort
class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        result = max(special[0]-bottom, top-special[-1])
        for i in range(1, len(special)):
            result = max(result, special[i]-special[i-1]-1)
        return result
