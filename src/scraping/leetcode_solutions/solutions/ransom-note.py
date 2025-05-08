# Time:  O(n)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        counts = [0] * 26
        letters = 0

        for c in ransomNote:
            if counts[ord(c) - ord('a')] == 0:
                letters += 1
            counts[ord(c) - ord('a')] += 1

        for c in magazine:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] == 0:
                letters -= 1
                if letters == 0:
                    break

        return letters == 0

# Time:  O(n)
import collections

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

