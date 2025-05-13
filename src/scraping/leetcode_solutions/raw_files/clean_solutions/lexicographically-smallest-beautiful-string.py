# Time:  O(n)

# greedy
class Solution(object):
    def smallestBeautifulString(self, s, k):
        def check(i):
            return (i-1 < 0 or arr[i-1] != arr[i]) and (i-2 < 0 or arr[i-2] != arr[i])

        arr = [ord(x)-ord('a') for x in s]
        for i in reversed(range(len(arr))):
            arr[i] += 1
            while not check(i):
                arr[i] += 1
            if arr[i] < k:
                break
        else:
            return ""
        for j in range(i+1, len(arr)):
            arr[j] = 0
            while not check(j):
                arr[j] += 1
        return "".join([chr(ord('a')+x) for x in arr])
