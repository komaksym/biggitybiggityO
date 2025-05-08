# Time:  O(t * m * n), t is target

class Solution(object):
    def minimizeTheDifference(self, mat, target):
        
        chosen_min = sum(min(row) for row in mat)
        if chosen_min >= target:
            return chosen_min-target
        dp = {0}
        for row in mat:
            dp = {total+x for total in dp for x in row if (total+x)-target < target-chosen_min}
        return min(abs(target-total) for total in dp)
