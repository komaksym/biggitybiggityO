# Time:  O(n + n * (log10(9k)/k) + ... + k)
#      = O((n - (log10(9k)/k)*k)/(1-log10(9k)/k))
#      = O(n / (1-log10(9k)/k)) = O(n) for k >= 2

# simulation
class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            s = "".join(map(str, (sum(map(int, s[i:i+k])) for i in range(0, len(s), k))))
        return s
