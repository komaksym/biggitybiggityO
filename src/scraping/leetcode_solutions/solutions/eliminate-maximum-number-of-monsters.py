# Time:  O(nlogn)

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        
        for i in range(len(dist)):
            dist[i] = (dist[i]-1)//speed[i]
        dist.sort()
        result = 0
        for i in range(len(dist)):
            if result > dist[i]:
                break
            result += 1
        return result
