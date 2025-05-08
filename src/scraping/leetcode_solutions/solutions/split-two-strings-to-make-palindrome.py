# Time:  O(n)

class Solution(object):
    def checkPalindromeFormation(self, a, b):
        
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(a, b):
            i, j = 0, len(b)-1
            while i < j:
                if a[i] != b[j]:
                    return is_palindrome(a, i, j) or is_palindrome(b, i, j)
                i += 1
                j -= 1
            return True

        return check(a, b) or check(b, a)
