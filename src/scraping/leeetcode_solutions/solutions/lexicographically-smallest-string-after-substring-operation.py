# Time:  O(n)

# greedy
class Solution(object):
    def smallestString(self, s):
        
        result = list(s)
        i = next((i for i in range(len(s)) if s[i] != 'a'), len(s))
        if i == len(s):
            result[-1] = 'z'
        else:
            for i in range(i, len(s)):
                if result[i] == 'a':
                    break
                result[i] = chr(ord(result[i])-1)
        return "".join(result)
