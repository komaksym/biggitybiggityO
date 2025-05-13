# Time:  O(nlogn)

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        order = list(range(len(growTime)))
        order.sort(key=lambda x: growTime[x], reverse=True)
        result = curr = 0
        for i in order:
            curr += plantTime[i]
            result = max(result, curr+growTime[i])
        return result
