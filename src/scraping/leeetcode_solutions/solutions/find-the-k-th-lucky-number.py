# Time:  O(logn)

# math, bitmasks
class Solution(object):
    def kthLuckyNumber(self, k):
        
        result = []
        k += 1
        while k != 1:
            result.append('7' if k&1 else '4')
            k >>= 1
        result.reverse()
        return "".join(result)


# Time:  O(logn)
# math, bitmasks
class Solution2(object):
    def kthLuckyNumber(self, k):
        
        return bin(k+1)[3:].replace('1', '7').replace('0', '4')
