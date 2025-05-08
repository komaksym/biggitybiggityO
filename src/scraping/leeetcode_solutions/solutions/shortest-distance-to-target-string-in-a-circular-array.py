# Time:  O(n)

# array
class Solution(object):
    def closetTarget(self, words, target, startIndex):
        
        INF = float("inf")
        result = INF
        for i, w in enumerate(words):
            if w == target:
                result = min(result, (i-startIndex)%len(words), (startIndex-i)%len(words))
        return result if result != INF else -1
