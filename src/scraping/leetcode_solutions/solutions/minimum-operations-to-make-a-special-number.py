# Time:  O(n)

# math, greedy
class Solution(object):
    def minimumOperations(self, num):
        lookup = [0]*10
        for i in reversed(range(len(num))):
            if ((num[i] in "05" and lookup[0]) or
                (num[i] in "27" and lookup[5])):
                return (len(num)-i)-2
            lookup[ord(num[i])-ord('0')] = 1
        return len(num)-lookup[0]
