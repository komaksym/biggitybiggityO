# Time:  O(m * n)

class Solution(object):
    def countSubstrings(self, s, t):
        def count(i, j):  # for each possible alignment, count the number of substrs that differ by 1 char
            result = left_cnt = right_cnt = 0  # left and right consecutive same counts relative to the different char
            for k in range(min(len(s)-i, len(t)-j)):
                right_cnt += 1
                if s[i+k] != t[j+k]:
                    left_cnt, right_cnt = right_cnt, 0
                result += left_cnt  # target substrs are [s[left_i+c:i+k+1] for c in xrange(left_cnt)]
            return result

        return sum(count(i, 0) for i in range(len(s))) + \
               sum(count(0, j) for j in range(1, len(t)))
