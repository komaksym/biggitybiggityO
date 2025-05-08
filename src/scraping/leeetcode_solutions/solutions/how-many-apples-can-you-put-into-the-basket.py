# Time:  O(nlogn)

class Solution(object):
    def maxNumberOfApples(self, arr):
        
        LIMIT = 5000
        arr.sort()
        result, total = 0, 0
        for x in arr:
            if total+x > LIMIT:
                break
            total += x
            result += 1
        return result
