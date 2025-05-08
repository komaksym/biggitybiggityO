# Time:  O(nlogn)

import math


class Solution(object):
    def visiblePoints(self, points, angle, location):
        
        arr, extra = [], 0
        for p in points:
            if p == location:
                extra += 1
                continue
            arr.append(math.atan2(p[1]-location[1], p[0]-location[0]))
        arr.sort()
        arr.extend([x + 2.0*math.pi for x in arr]) 
        d = 2.0*math.pi * (angle/360.0)
        left = result = 0
        for right in range(len(arr)):
            while arr[right]-arr[left] > d:
                left += 1
            result = max(result, right-left+1)
        return result + extra
