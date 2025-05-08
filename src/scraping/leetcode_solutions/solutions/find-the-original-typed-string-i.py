# Time:  O(n)

# array
class Solution(object):
    def possibleStringCount(self, word):
        
        return len(word)-sum(word[i] != word[i+1] for i in range(len(word)-1))


# Time:  O(n)
# array
class Solution2(object):
    def possibleStringCount(self, word):
        
        result = 1
        curr = 0
        for i in range(len(word)):
            curr += 1
            if i+1 == len(word) or word[i+1] != word[i]:
                result += curr-1
                curr = 0
        return result
