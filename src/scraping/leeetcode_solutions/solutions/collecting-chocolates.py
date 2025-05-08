# Time:  O(n)

# mono stack, difference array, prefix sum
class Solution(object):
    def minCost(self, nums, x):
        
        def accumulate(a):
            for i in range(len(a)-1):
                a[i+1] += a[i]
            return a

        i = min(range(len(nums)), key=lambda x: nums[x])
        nums = nums[i:]+nums[:i]
        left, right = [-1]*len(nums), [len(nums)]*len(nums)
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]] > nums[i]:
                right[stk.pop()] = i
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        diff2 = [0]*(len(nums)+1)
        diff2[0] = (+1)*sum(nums)            
        diff2[1] = x                         
        diff2[-1] += (-1)*nums[0]            
        for i in range(1, len(nums)):
            l, r = i-left[i], right[i]-i
            diff2[min(l, r)] += (-1)*nums[i] 
            diff2[max(l, r)] += (-1)*nums[i] 
            diff2[l+r] += (+1)*nums[i]       
        return min(accumulate(accumulate(diff2)))


# Time:  O(nlogn)
import collections


# binary search, mono deque
class Solution2(object):
    def minCost(self, nums, x):
        
        def cost(k):
            w = k+1
            result = x*k
            dq = collections.deque()
            for i in range(len(nums)+w-1):
                if dq and i-dq[0] == w:
                    dq.popleft()
                while dq and nums[dq[-1]%len(nums)] >= nums[i%len(nums)]:
                    dq.pop()
                dq.append(i)
                if i >= w-1:
                    result += nums[dq[0]%len(nums)]
            return result

        def check(x):
            return cost(x) <= cost(x+1)

        left, right = 0, len(nums)
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return cost(left)


# Time:  O(n^2)
# brute force
class Solution3(object):
    def minCost(self, nums, x):
        
        result = [x*k for k in range(len(nums)+1)]
        for i in range(len(nums)):
            curr = nums[i]
            for k in range(len(result)):
                curr = min(curr, nums[(i+k)%len(nums)])
                result[k] += curr
        return min(result)
