# Time:  O(nlogn)

class Solution(object):
    def findBestValue(self, arr, target):
        
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
       
       
       
       
       
       
        return max_arr if not arr else (2*target+len(arr)-1)//(2*len(arr))


# Time:  O(nlogn)
class Solution2(object):
    def findBestValue(self, arr, target):
        
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        if not arr:
            return max_arr
        x = (target-1)//len(arr)
        return x if target-x*len(arr) <= (x+1)*len(arr)-target else x+1


# Time:  O(nlogm), m is the max of arr, which may be larger than n
class Solution3(object):
    def findBestValue(self, arr, target):
        
        def total(arr, v):
            result = 0
            for x in arr:
                result += min(v, x)
            return result

        def check(arr, v, target):
            return total(arr, v) >= target
        
        left, right = 1, max(arr)
        while left <= right:
            mid = left + (right-left)//2
            if check(arr, mid, target):
                right = mid-1
            else:
                left = mid+1
        return left-1 if target-total(arr, left-1) <= total(arr, left)-target else left
