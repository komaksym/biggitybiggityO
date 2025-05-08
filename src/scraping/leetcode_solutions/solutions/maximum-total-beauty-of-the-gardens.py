# Time:  O(nlogn)

import bisect


# sort, prefix sum, greedy, two pointers, improved from solution3
class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix, suffix = 0, sum(flowers[i] for i in range(n))
        result = left = 0
        for right in range(n+1):
            if right:
                suffix -= flowers[right-1]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            while not (left == right or (left and (total+prefix)//left <= flowers[left])):
                prefix += flowers[left]
                left += 1
            mn = min((total+prefix)//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result


# Time:  O(nlogn)
import bisect


# sort, prefix sum, greedy, two pointers, improved from solution4
class Solution2(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+flowers[i]
        result = suffix = 0
        left = n
        for right in reversed(range(n+1)):
            if right != n:
                suffix += flowers[right]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            left = min(left, right)
            while not (left == 0 or (prefix[left]-prefix[left-1])*left-prefix[left] <= total):
                left -= 1
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result


# Time:  O(nlogn)
import bisect


# sort, prefix sum, greedy, binary search
class Solution3(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        def check(prefix, total, x):
            return x and (total+prefix[x])//x <= prefix[x+1]-prefix[x]

        def binary_search(prefix, total, left, right):
            while left <= right:
                mid = left+(right-left)//2
                if check(prefix, total, mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
    
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+flowers[i]
        suffix = sum(flowers[i] for i in range(n))
        result = left = 0
        for right in range(n+1):
            if right:
                suffix -= flowers[right-1]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            left = binary_search(prefix, total, 0, right-1)
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result


# Time:  O(nlogn)
import bisect


# sort, prefix sum, greedy, binary search
class Solution4(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        def check(prefix, total, x):
            return (prefix[x]-prefix[x-1])*x-prefix[x] <= total

        def binary_search_right(prefix, total, left, right):
            while left <= right:
                mid = left+(right-left)//2
                if not check(prefix, total, mid):
                    right = mid-1
                else:
                    left = mid+1
            return right
    
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+flowers[i]
        result = suffix = 0
        left = n
        for right in reversed(range(n+1)):
            if right != n:
                suffix += flowers[right]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                break
            left = binary_search_right(prefix, total, 1, right)
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result
