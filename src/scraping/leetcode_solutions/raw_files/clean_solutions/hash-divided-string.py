from functools import reduce
# Time:  O(n)

# string
class Solution(object):
    def stringHash(self, s, k):
        result = (chr(ord('a')+reduce(lambda accu, x: (accu+x)%26,  (ord(s[i+j])-ord('a') for j in range(k)), 0)) for i in range(0, len(s), k))
        return "".join(result)
