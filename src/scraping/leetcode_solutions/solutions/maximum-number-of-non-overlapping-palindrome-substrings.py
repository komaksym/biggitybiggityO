# Time:  O(n * k)

# two pointers, greedy
class Solution(object):
    def maxPalindromes(self, s, k):
        result = prev = 0
        for mid in range(2*len(s)-1):
            left, right = mid//2, mid//2+mid%2
            while left >= prev and right < len(s) and s[left] == s[right]:
                if right-left+1 >= k:
                    prev = right+1
                    result += 1
                    break
                left, right = left-1, right+1
        return result
