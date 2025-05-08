# Time:  O(n)

# rolling hash
class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        
        h, idx = 0, -1
        pw = pow(power, k-1, modulo)
        for i in reversed(range(len(s))):
            if i+k < len(s):
                h = (h-(ord(s[i+k])-ord('a')+1)*pw)%modulo
            h = (h*power+(ord(s[i])-ord('a')+1))%modulo
            if h == hashValue:
                idx = i
        return s[idx:idx+k]
