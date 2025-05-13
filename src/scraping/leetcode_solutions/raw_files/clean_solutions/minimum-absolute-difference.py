# Time:  O(nlogn)

class Solution(object):
    def minimumAbsDifference(self, arr):
        result = []
        min_diff = float("inf")
        arr.sort()
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
