# Time:  O(n)

class Solution(object):
    def countBits(self, num):
        
        res = [0]
        for i in range(1, num + 1):
           
            res.append((i & 1) + res[i >> 1])
        return res

    def countBits2(self, num):
        
        s = [0]
        while len(s) <= num:
            s.extend([x + 1 for x in s])
        return s[:num + 1]


