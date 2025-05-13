# Time:  O(n)

# two pointers, sliding window
class Solution(object):
    def numberOfSpecialSubstrings(self, s):
        result = left = 0
        lookup = [-1]*26
        for right in range(len(s)):
            if lookup[ord(s[right])-ord('a')] >= left:
                left = lookup[ord(s[right])-ord('a')]+1
            lookup[ord(s[right])-ord('a')] = right
            result += (right-left+1)
        return result


# Time:  O(n)
# two pointers, sliding window
class Solution2(object):
    def numberOfSpecialSubstrings(self, s):
        result = left = 0
        lookup = [False]*26
        for right in range(len(s)):
            while lookup[ord(s[right])-ord('a')]:
                lookup[ord(s[left])-ord('a')] = False
                left += 1
            lookup[ord(s[right])-ord('a')] = True
            result += (right-left+1)
        return result
