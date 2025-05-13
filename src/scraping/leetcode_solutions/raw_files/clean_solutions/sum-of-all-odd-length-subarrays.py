# Time:  O(n)

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        def ceil_divide(a, b):
            return (a+(b-1))//b
        return sum(x * ceil_divide((i-0+1)*((len(arr)-1)-i+1), 2) for i, x in enumerate(arr))
