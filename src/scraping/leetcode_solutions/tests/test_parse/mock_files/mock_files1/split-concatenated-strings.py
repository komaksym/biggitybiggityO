# Time:  O(n^2)

class Solution(object):
    def splitLoopedString(self, strs):
        tmp = []
        for s in strs:
            tmp += max(s, s[::-1])
        s = "".join(tmp)

        result, st = "a", 0
        for i in range(len(strs)):
            body = "".join([s[st + len(strs[i]):], s[0:st]])
            for p in strs[i], strs[i][::-1]:
                for j in range(len(strs[i])):
                    if p[j] >= result[0]:
                        result = max(result, "".join([p[j:], body, p[:j]]))
            st += len(strs[i])
        return result

