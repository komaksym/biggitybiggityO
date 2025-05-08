# Time:  O(n)


class Solution(object):
    def isOneBitCharacter(self, bits):
        
        parity = 0
        for i in reversed(range(len(bits)-1)):
            if bits[i] == 0:
                break
            parity ^= bits[i]
        return parity == 0

