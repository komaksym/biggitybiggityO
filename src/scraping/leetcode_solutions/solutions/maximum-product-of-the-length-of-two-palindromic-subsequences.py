# Time:  O(3^n)

class Solution(object):
    def maxProduct(self, s):
        def palindromic_subsequence_length(s, mask):
            result = 0
            left, right = 0, len(s)-1
            left_bit, right_bit = 1<<left, 1<<right
            while left <= right:
                if mask&left_bit == 0:
                    left, left_bit = left+1, left_bit<<1
                elif mask&right_bit == 0:
                    right, right_bit = right-1, right_bit>>1
                elif s[left] == s[right]:
                    result += 1 if left == right else 2
                    left, left_bit = left+1, left_bit<<1
                    right, right_bit = right-1, right_bit>>1
                else:
                    return 0
            return result
        
        dp = [palindromic_subsequence_length(s, mask) for mask in range(1<<len(s))]
        result = 0
        for mask in range(len(dp)):
            if dp[mask]*(len(s)-dp[mask]) <= result:  # optimize
                continue
            submask = inverse_mask = (len(dp)-1)^mask
            while submask:
                result = max(result, dp[mask]*dp[submask])
                submask = (submask-1)&inverse_mask
        return result
