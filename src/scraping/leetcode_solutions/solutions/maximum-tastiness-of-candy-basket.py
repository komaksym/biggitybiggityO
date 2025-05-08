# Time:  O(nlogr), r = max(price)-min(price)

# binary search, greedy
class Solution(object):
    def maximumTastiness(self, price, k):
        
        def check(x): 
            cnt = prev = 0
            for i in range(len(price)):
                if prev and price[i]-prev < x:
                    continue
                cnt += 1
                if cnt == k:
                    break
                prev = price[i]
            return cnt >= k

        price.sort()
        left, right = 1, price[-1]-price[0]
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right
