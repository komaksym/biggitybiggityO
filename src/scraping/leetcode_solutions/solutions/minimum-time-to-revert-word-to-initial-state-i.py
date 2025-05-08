# Time:  O(n)

# z-function
class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        def z_function(s): 
            z = [0]*len(s)
            l, r = 0, 0
            for i in range(1, len(z)):
                if i <= r:
                    z[i] = min(r-i+1, z[i-l])
                while i+z[i] < len(z) and s[z[i]] == s[i+z[i]]:
                    z[i] += 1
                if i+z[i]-1 > r:
                    l, r = i, i+z[i]-1
            return z

        z = z_function(word)
        for i in range(k, len(word), k):
            if z[i] == len(word)-i:
                return i//k
        return ceil_divide(len(word), k)


# Time:  O(n^2)
# brute force
class Solution2(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        for i in range(k, len(word), k):
            if all(word[i+j] == word[j] for j in range(len(word)-i)):
                return i//k
        return ceil_divide(len(word), k)
