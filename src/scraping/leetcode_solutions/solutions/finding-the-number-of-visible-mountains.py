# Time:  O(nlogn)

# math, sort
class Solution(object):
    def visibleMountains(self, peaks):
        """
        :type peaks: List[List[int]]
        :rtype: int
        """
        peaks.sort(key=lambda x: (x[0]-x[1], -(x[0]+x[1]))) 
        result = mx = 0
        for i in range(len(peaks)):
            if peaks[i][0]+peaks[i][1] <= mx:
                continue
            mx = peaks[i][0]+peaks[i][1]
            if i+1 == len(peaks) or peaks[i+1] != peaks[i]:
                result += 1
        return result


# Time:  O(nlogn)
# sort, mono stack
class Solution2(object):
    def visibleMountains(self, peaks):
        """
        :type peaks: List[List[int]]
        :rtype: int
        """
        def is_covered(a, b):
            x1, y1 = a
            x2, y2 = b
            return x2-y2 <= x1-y1 and x1+y1 <= x2+y2

        peaks.sort()
        stk = []
        for i in range(len(peaks)):
            while stk and is_covered(peaks[stk[-1]], peaks[i]):
                stk.pop()
            if (i-1 == -1 or peaks[i-1] != peaks[i]) and (not stk or not is_covered(peaks[i], peaks[stk[-1]])): 
                stk.append(i)
        return len(stk)
            
