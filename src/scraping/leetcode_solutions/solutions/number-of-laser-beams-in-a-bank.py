# Time:  O(m * n)

class Solution(object):
    def numberOfBeams(self, bank):
        result = prev = 0
        for x in bank:
            cnt = x.count('1')
            if not cnt:
                continue
            result += prev*cnt
            prev = cnt
        return result
