# Time:  O(nlogn)

# sort, prefix sum, two pointers, sliding window
class Solution(object):
    def minConnectedGroups(self, intervals, k):
        intervals.sort()
        result = 0
        prefix = [0]*(len(intervals)+1)
        mx = float("-inf")
        left = 0
        for right in range(len(intervals)):
            prefix[right+1] = prefix[right]+int(mx < intervals[right][0])
            mx = max(mx, intervals[right][1])
            while intervals[right][0]-intervals[left][1] > k:
                left += 1
            result = max(result, prefix[right+1]-prefix[left+1])
        return prefix[-1]-result
