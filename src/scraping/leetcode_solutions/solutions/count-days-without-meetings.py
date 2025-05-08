# Time:  O(nlogn)

# sort
class Solution(object):
    def countDays(self, days, meetings):
        meetings.sort()
        result = curr = 0
        for s, e in meetings:
            result += max((s-1)-curr, 0)
            curr = max(curr, e)
        result += days-curr
        return result
