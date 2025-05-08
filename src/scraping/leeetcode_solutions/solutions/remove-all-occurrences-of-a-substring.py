# Time:  O(n + m)

# kmp solution
class Solution(object):
    def removeOccurrences(self, s, part):
        
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j != -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        
        prefix = getPrefix(part)
        result, lookup = [], []
        i = -1
        for c in s:
            while i != -1 and part[i+1] != c:
                i = prefix[i]
            if part[i+1] == c:
                i += 1
            result.append(c)
            lookup.append(i)
            if i == len(part)-1:
                result[len(result)-len(part):] = []
                lookup[len(lookup)-len(part):] = []
                i = lookup[-1] if lookup else -1
        return "".join(result)
