# Time:  O(n)

# math
class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        
        total = mn = mx = 0
        for x in differences:
            total += x
            mn = min(mn, total)
            mx = max(mx, total)
        return max((upper-lower)-(mx-mn)+1, 0)
