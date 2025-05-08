# Time:  O(n + q)

# prefix sum
class Solution(object):
    def vowelStrings(self, words, queries):
        
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0]*(len(words)+1)
        for i, w in enumerate(words):
            prefix[i+1] = prefix[i]+int(w[0] in VOWELS and w[-1] in VOWELS)
        return [prefix[r+1]-prefix[l] for l, r in queries]
