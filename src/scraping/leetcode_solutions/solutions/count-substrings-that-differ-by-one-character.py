# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def count(i, j): 
            result = left_cnt = right_cnt = 0 
            for k in range(min(len(s)-i, len(t)-j)):
                right_cnt += 1
                if s[i+k] != t[j+k]:
                    left_cnt, right_cnt = right_cnt, 0
                result += left_cnt 
            return result

        return sum(count(i, 0) for i in range(len(s))) + \
               sum(count(0, j) for j in range(1, len(t)))
