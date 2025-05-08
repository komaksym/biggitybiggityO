# Time:  O(n)

# two pointers, sliding window
class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        startTime.append(eventTime)
        endTime.insert(0, 0)
        result = curr = 0
        for i in range(len(startTime)):
            curr += startTime[i]-endTime[i]
            result = max(result, curr)
            if i-k >= 0:
                curr -= startTime[i-k]-endTime[i-k]
        return result
