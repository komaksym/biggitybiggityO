# Time:  O(logn)

class Solution(object):
    def maximum69Number (self, num):
        
        curr, base, change = num, 3, 0
        while curr:
            if curr%10 == 6:
                change = base
            base *= 10
            curr //= 10
        return num+change


# Time:  O(logn)
class Solution2(object):
    def maximum69Number (self, num):
        
        return int(str(num).replace('6', '9', 1))
