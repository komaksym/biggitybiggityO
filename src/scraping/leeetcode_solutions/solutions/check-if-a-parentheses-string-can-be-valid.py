# Time:  O(n)

class Solution(object):
    def canBeValid(self, s, locked):
        
        if len(s)%2:
            return False
        for direction, c in ((lambda x:x, '('), (reversed, ')')):
            cnt = bal = 0
            for i in direction(range(len(s))):
                if locked[i] == '0':
                    cnt += 1
                else:
                    bal += 1 if s[i] == c else -1
                    if cnt+bal < 0:
                        return False
        return True
