# Time:  O(n)

class Solution(object):
    def getWinner(self, arr, k):
        
        result = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > result:
                result = arr[i]
                count = 0
            count += 1
            if (count == k):
                break
        return result
