# Time:  O(n)

# string
class Solution(object):
    def compressedString(self, word):
        
        result = []
        cnt = 0
        for i in range(len(word)):
            cnt += 1
            if cnt == 9 or (i+1 == len(word) or word[i+1] != word[i]):
                result.append("%s%s" % (cnt, word[i]))
                cnt = 0
        return "".join(result)
