# Time:  O(n^0.25 * logn)

class Solution(object):
    def superpalindromesInRange(self, L, R):
        
        def is_palindrome(k):
            return str(k) == str(k)[::-1]

        K = int((10**((len(R)+1)*0.25)))
        l, r = int(L), int(R)

        result = 0

       
        for k in range(K):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t)**2
            if v > r:
                break
            if v >= l and is_palindrome(v):
                result += 1

       
        for k in range(K):
            s = str(k)
            t = s + s[::-1]
            v = int(t)**2
            if v > r:
                break
            if v >= l and is_palindrome(v):
                result += 1

        return result

