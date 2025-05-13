# Time:  O(n)

# two pointers
class Solution(object):
    def clearDigits(self, s):
        s = list(s)
        j = 0
        for i, x in enumerate(s):
            if x.isdigit():
                j -= 1
                continue
            s[j] = x
            j += 1
        while len(s) > j:
            s.pop()
        return "".join(s)


# Time:  O(n)
# stack
class Solution2(object):
    def clearDigits(self, s):
        result = []
        for x in s:
            if x.isdigit():
                result.pop()
                continue
            result.append(x)
        return "".join(result)
