# Time:  O(n + 26)

# counting sort, greedy
class Solution(object):
    def makeAntiPalindrome(self, s):
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [i for i, x in enumerate(cnt) for _ in range(x)]
        l = next(l for l in range((len(s)//2)//2+1) if result[len(s)//2+l] != result[len(s)//2-1])
        if l:
            for i in range(cnt[result[len(s)//2-1]]-l):
                result[len(s)//2+i], result[len(s)//2+i+l] = result[len(s)//2+i+l], result[len(s)//2+i]
        return "".join([chr(ord('a')+x) for x in result])


# Time:  O(n + 26)
# counting sort, greedy, two pointers
class Solution2(object):
    def makeAntiPalindrome(self, s):
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [i for i, x in enumerate(cnt) for _ in range(x)]
        left = len(s)//2
        right = left+1
        while right < len(s) and result[right] == result[left]:
            right += 1 
        while result[left] == result[len(s)-1-left]:
            result[left] , result[right] = result[right], result[left]
            left += 1
            right += 1
        return "".join([chr(ord('a')+x) for x in result])
# freq table, greedy
class Solution3(object):
    def makeAntiPalindrome(self, s):
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [-1]*len(s)
        for i in range(len(s)//2):
            j = next(j for j in range(len(cnt)) if cnt[j])
            cnt[j] -= 1
            result[i] = j
        for i in range(len(s)//2, len(s)):
            j = next(j for j in range(len(cnt)) if cnt[j] and result[(len(s)-1)-i] != j)
            cnt[j] -= 1
            result[i] = j
        return "".join([chr(ord('a')+x) for x in result])
