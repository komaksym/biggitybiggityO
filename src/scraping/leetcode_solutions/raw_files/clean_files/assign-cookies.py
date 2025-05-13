# Time:  O(nlogn)


class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        result, i = 0, 0
        for j in range(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                result += 1
                i += 1
        return result

