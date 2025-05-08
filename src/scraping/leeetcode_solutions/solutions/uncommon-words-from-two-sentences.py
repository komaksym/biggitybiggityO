# Time:  O(m + n)

import collections

    
class Solution(object):
    def uncommonFromSentences(self, A, B):
        
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        return [word for word in count if count[word] == 1]

