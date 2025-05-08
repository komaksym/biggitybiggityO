# Time:  O(logn)

class Solution(object):
    def pathInZigZagTree(self, label):
        count = 2**label.bit_length()
        result = []
        while label >= 1:
            result.append(label)
            label = ((count//2) + ((count-1)-label)) // 2
            count //= 2
        result.reverse()
        return result
