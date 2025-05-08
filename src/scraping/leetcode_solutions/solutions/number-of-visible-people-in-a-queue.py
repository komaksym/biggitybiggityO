# Time:  O(n)

class Solution(object):
    def canSeePersonsCount(self, heights):
        result = [0]*len(heights)
        stk = []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] < h:
                result[stk.pop()] += 1
            if stk:
                result[stk[-1]] += 1
            if stk and heights[stk[-1]] == h:
                stk.pop()
            stk.append(i)
        return result


# Time:  O(n)
class Solution2(object):
    def canSeePersonsCount(self, heights):
        result = [0]*len(heights)
        stk = []
        for i in reversed(range(len(heights))):
            cnt = 0
            while stk and heights[stk[-1]] < heights[i]:
                stk.pop()
                cnt += 1
            result[i] = cnt+1 if stk else cnt
            if stk and heights[stk[-1]] == heights[i]:
                stk.pop()
            stk.append(i)
        return result
