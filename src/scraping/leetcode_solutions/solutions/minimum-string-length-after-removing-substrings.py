# Time:  O(n)

# stack
class Solution(object):
    def minLength(self, s):
        stk = []
        for c in s:
            if stk and ((stk[-1] == 'A' and c == 'B') or (stk[-1] == 'C' and c == 'D')):
                stk.pop()
                continue
            stk.append(c)
        return len(stk)
