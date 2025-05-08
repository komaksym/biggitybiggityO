# Time:  O(n)

class Solution(object):
    def containsPattern(self, arr, m, k):
        
        cnt = 0
        for i in range(len(arr)-m):
            if arr[i] != arr[i+m]:
                cnt = 0
                continue
            cnt += 1
            if cnt == (k-1)*m:
                return True
        return False
