# Time:  O(nlogn)

class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1]-x[0]) 
        result = 0
        for a, m in tasks: 
            result = max(result+a, m)
        return result


# Time:  O(nlogn)
class Solution2(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[0]-x[1]) 
        result = curr = 0
        for a, m in tasks: 
            result += max(m-curr, 0)
            curr = max(curr, m)-a
        return result
