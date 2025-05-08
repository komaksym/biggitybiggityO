# Time:  O(n * sqrt(n)) = O(n^(3/2))

# two pointers, sliding window
class Solution(object):
    def numberOfSubstrings(self, s):
        
        result = 0
        idxs = [-1]+[i for i, x in enumerate(s) if x == '0']+[len(s)]
        curr = 1
        for i in range(len(s)):
            if idxs[curr] == i:
                curr += 1
            for c in range(min(int((-1+(1+4*(i+1))**0.5)/2)+1, curr)): 
                if c**2 <= (i-idxs[(curr-c)-1])-c:
                    result += min(min(idxs[curr-c], i)-idxs[(curr-c)-1], ((i-idxs[(curr-c)-1])-c)-c**2+1)
        return result


# Time:  O(n * sqrt(n)) = O(n^(3/2))
# two pointers, sliding window
class Solution2(object):
    def numberOfSubstrings(self, s):
        
        result = 0
        idxs = [-1]+[i for i, x in enumerate(s) if x == '0']+[len(s)]
        for c in range(int((-1+(1+4*len(s))**0.5)/2)+1): 
            left = right = 1
            for i in range(len(s)):
                if idxs[right] == i:
                    right += 1
                if right-left == c+1:
                    left += 1
                if not (right-left == c and ((i-idxs[left-1])-c) >= c**2):
                    continue
                result += min(min(idxs[left], i)-idxs[left-1], ((i-idxs[left-1])-c)-c**2+1)
        return result


# Time:  O(n * sqrt(n)) = O(n^(3/2))
# two pointers, sliding window
class Solution_TLE(object):
    def numberOfSubstrings(self, s):
        
        result = 0
        for c in range(int((-1+(1+4*len(s))**0.5)/2)+1): 
            cnt = [0]*2
            left = curr = 0
            for right in range(len(s)):
                cnt[s[right] == '1'] += 1
                while cnt[0] == c+1:
                    cnt[s[left] == '1'] -= 1
                    left += 1
                if not (cnt[0] == c and cnt[1] >= c**2):
                    continue
                for curr in range(max(curr, left), right):
                    if s[curr] == '0':
                        break
                else:
                    curr = right
                result += min(curr-left+1, cnt[1]-c**2+1)
        return result
