# Time:  O(32 * n)

class Solution(object):
    def subarrayBitwiseORs(self, A):
        result, curr = set(), {0}
        for i in A:
            curr = {i} | {i | j for j in curr}
            result |= curr
        return len(result)

