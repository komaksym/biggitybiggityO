# Time:  O(logr) = O(1)

# bitmasks
class Solution(object):
    def kthCharacter(self, k, operations):
        result = 0
        k -= 1
        for i in range(min(len(operations), k.bit_length())):
            if k&(1<<i):
                result = (result+operations[i])%26
        return chr(ord('a')+result)
