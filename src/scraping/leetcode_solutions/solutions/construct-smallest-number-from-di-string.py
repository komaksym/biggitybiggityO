# Time:  O(n)

# constructive algorithms
class Solution(object):
    def smallestNumber(self, pattern):
        
        result = []
        for i in range(len(pattern)+1):
            if not (i == len(pattern) or pattern[i] == 'I'):
                continue
            for x in reversed(list(range(len(result)+1, (i+1)+1))):
                result.append(x)
        return "".join(map(str, result))
