# Time:  O(logn)

class Solution(object):
    def confusingNumber(self, N):
        
        lookup = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        S = str(N)
        result = []
        for i in range(len(S)):
            if S[i] not in lookup:
                return False
        for i in range((len(S)+1)//2):
            if S[i] != lookup[S[-(i+1)]]:
                return True
        return False
