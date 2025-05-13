# Time:  O(n)

# greedy
class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        return [words[i] for i in range(n) if i == 0 or groups[i-1] != groups[i]]
