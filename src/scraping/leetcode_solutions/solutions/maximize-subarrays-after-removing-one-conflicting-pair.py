# Time:  O(n + m)

# greedy
class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        right = [[] for _ in range(n)]
        for l, r in conflictingPairs:
            l, r = l-1, r-1
            if l > r:
                l, r = r, l
            right[r].append(l)
        result = 0
        top2 = [-1]*2
        cnt = [0]*n
        for r in range(n):
            for l in right[r]:
                for i in range(len(top2)):
                    if l > top2[i]:
                        l, top2[i] = top2[i], l
            result += r-top2[0]
            if top2[0] != -1:
                cnt[top2[0]] += top2[0]-top2[1]
        return result+max(cnt)
