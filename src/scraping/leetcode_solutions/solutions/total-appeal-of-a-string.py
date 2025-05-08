# Time:  O(n)

# combinatorics
class Solution(object):
    def appealSum(self, s):
        
        result = curr = 0
        lookup = [-1]*26
        for i, c in enumerate(s):
            result += (i-lookup[ord(c)-ord('a')])*(len(s)-i)
            lookup[ord(c)-ord('a')] = i
        return result


# Time:  O(n)
# counting
class Solution2(object):
    def appealSum(self, s):
        
        result = cnt = 0
        lookup = [-1]*26
        for i, c in enumerate(s):
            cnt += i-lookup[ord(c)-ord('a')]
            lookup[ord(c)-ord('a')] = i
            result += cnt
        return result

