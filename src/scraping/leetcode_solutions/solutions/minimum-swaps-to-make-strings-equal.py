# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        x1, y1 = 0, 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            x1 += int(s1[i] == 'x')
            y1 += int(s1[i] == 'y')
        if x1%2 !=  y1%2:  # impossible
            return -1
        return (x1//2 + y1//2) + (x1%2 + y1%2)
