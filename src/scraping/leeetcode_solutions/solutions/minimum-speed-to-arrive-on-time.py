# Time:  O(nlogr), r is the range of speed

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        
        def ceil(a, b):
            return (a+b-1)//b

        def total_time(dist, x):
            return sum(ceil(dist[i], x) for i in range(len(dist)-1)) + float(dist[-1])/x

        def check(dist, hour, x):
            return total_time(dist, x) <= hour

        MAX_SPEED = 10**7
        if not check(dist, hour, MAX_SPEED):
            return -1
        left, right = 1, MAX_SPEED
        while left <= right:
            mid = left + (right-left)//2
            if check(dist, hour, mid):
                right = mid-1
            else:
                left = mid+1
        return left
