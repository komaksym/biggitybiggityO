# Time:  O(n)

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        
        i = 0
        s = []
        for v in pushed:
            s.append(v)
            while s and i < len(popped) and s[-1] == popped[i]:
                s.pop()
                i += 1
        return i == len(popped)
