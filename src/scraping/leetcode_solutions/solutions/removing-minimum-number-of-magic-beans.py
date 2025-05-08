# Time:  O(nlogn)

# math
class Solution(object):
    def minimumRemoval(self, beans):
        beans.sort()
        return sum(beans) - max(x*(len(beans)-i)for i, x in enumerate(beans))
