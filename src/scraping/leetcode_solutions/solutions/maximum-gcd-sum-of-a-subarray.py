# Time:  O(nlogr), r = max(nums)

# number theory, dp, prefix sum
class Solution(object):
    def maxGcdSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = prefix = 0
        dp = []
        for right, x in enumerate(nums):
            dp.append((right, x, prefix))
            prefix += x
            new_dp = []
            for left, g, p in dp: 
                ng = gcd(g, x) 
                if not new_dp or new_dp[-1][1] != ng:
                    new_dp.append((left, ng, p)) 
            dp = new_dp
            for left, g, p in dp:
                if right-left+1 < k:
                    break
                result = max(result, (prefix-p)*g)
        return result


# Time:  O(nlogr), r = max(nums)
# number theory, dp, prefix sum
class Solution2(object):
    def maxGcdSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        result = 0
        dp = []
        for right, x in enumerate(nums):
            dp.append((right, x))
            new_dp = []
            for left, g in dp: 
                ng = gcd(g, x) 
                if not new_dp or new_dp[-1][1] != ng:
                    new_dp.append((left, ng)) 
            dp = new_dp
            for left, g in dp:
                if right-left+1 < k:
                    break
                result = max(result, (prefix[right+1]-prefix[left])*g)
        return result


# Time:  O(n * logr * (logn * logr)) = O(n * (logr)^2 * logn), r = max(nums)
# number theory, binary search, rmq, sparse table, prefix sum
class Solution3_TLE(object):
    def maxGcdSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        class SparseTable(object):
            def __init__(self, arr, fn):
                self.fn = fn
                self.bit_length = [0]
                n = len(arr)
                k = n.bit_length()-1 
                for i in range(k+1):
                    self.bit_length.extend(i+1 for _ in range(min(1<<i, (n+1)-len(self.bit_length))))
                self.st = [[0]*n for _ in range(k+1)]
                self.st[0] = arr[:]
                for i in range(1, k+1): 
                    for j in range((n-(1<<i))+1):
                        self.st[i][j] = fn(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])
        
            def query(self, L, R): 
                i = self.bit_length[R-L+1]-1 
                return self.fn(self.st[i][L], self.st[i][R-(1<<i)+1])
        
        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        result = 0
        rmq = SparseTable(nums, gcd)
        for left, x in enumerate(nums):
            right = left
            while right < len(nums): 
                g = rmq.query(left, right)
                right = binary_search_right(right, len(nums)-1, lambda x: rmq.query(left, x) >= g) 
                if right-left+1 >= k:
                    result = max(result, (prefix[right+1]-prefix[left])*g)
                right += 1
        return result
