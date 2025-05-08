# Time:  O(n^2)

# sort, array
class Solution(object):
    def numberOfPairs(self, points):
        
        points.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        for i in range(len(points)):
            y = float("-inf")
            for j in range(i+1, len(points)):
                if points[i][1] < points[j][1]:
                    continue
                if points[j][1] > y:
                    y = points[j][1]
                    result += 1
        return result


# Time:  O(n^3)
# sort, array
class Solution2(object):
    def numberOfPairs(self, points):
        
        points.sort(key=lambda x: (x[0], -x[1]))
        return sum(all(not points[i][1] >= points[k][1] >= points[j][1] for k in range(i+1, j))
                   for i in range(len(points))
                   for j in range(i+1, len(points)) if points[i][1] >= points[j][1])
 
