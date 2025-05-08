# Time:  O(n)

class Solution(object):
    def duplicateZeros(self, arr):
        
        shift, i = 0, 0
        while i+shift < len(arr):
            shift += int(arr[i] == 0)
            i += 1
        i -= 1
        while shift:
            if i+shift < len(arr):
                arr[i+shift] = arr[i]
            if arr[i] == 0:
                shift -= 1
                arr[i+shift] = arr[i]
            i -= 1
