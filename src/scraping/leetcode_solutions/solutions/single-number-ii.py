# Time:  O(n)

import collections


class Solution(object):
   
   
    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one


class Solution2(object):
   
   
    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one


class Solution3(object):
    def singleNumber(self, nums):
        
        return list((collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys())[0]


class Solution4(object):
    def singleNumber(self, nums):
        
        return (sum(set(nums)) * 3 - sum(nums)) / 2


#  every element appears 4 times except for one with 2 times
class SolutionEX(object):
   
   
   
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two

