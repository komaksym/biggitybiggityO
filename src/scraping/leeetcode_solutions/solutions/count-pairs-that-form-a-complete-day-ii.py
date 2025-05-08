# Time:  O(n + 24)

# freq table
class Solution(object):
    def countCompleteDayPairs(self, hours):
        
        result = 0
        cnt = [0]*24
        for x in hours:
            result += cnt[-x%24]
            cnt[x%24] += 1
        return result
