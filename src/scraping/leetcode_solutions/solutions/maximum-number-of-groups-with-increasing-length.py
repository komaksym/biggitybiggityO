# Time:  O(n)

# constructive algorithms, counting sort, greedy
class Solution(object):
    def maxIncreasingGroups(self, usageLimits):
        def inplace_counting_sort(nums, reverse=False): 
            if not nums:
                return
            count = [0]*(max(nums)+1)
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(range(len(nums))): 
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in range(len(nums)):
                nums[i] = ~nums[i] 
            if reverse: 
                nums.reverse()

        usageLimits = [min(x, len(usageLimits)) for x in usageLimits]
        inplace_counting_sort(usageLimits)
        result = curr = 0
        for x in usageLimits:
            curr += x
            if curr >= result+1:
                curr -= result+1
                result += 1
        return result


# Time:  O(nlogn)
# constructive algorithms, sort, greedy
class Solution2(object):
    def maxIncreasingGroups(self, usageLimits):
        usageLimits.sort()
        result = curr = 0
        for x in usageLimits:
            curr += x
            if curr >= result+1:
                curr -= result+1
                result += 1
        return result

# constructive algorithms, sort, binary search, greedy
class Solution3(object):
    def maxIncreasingGroups(self, usageLimits):
        def check(l):
            curr = 0
            for i in range(l):
                curr += usageLimits[~i]-(l-i)
                curr = min(curr, 0)
            for i in range(len(usageLimits)-l):
                curr += usageLimits[i]
            return curr >= 0

        usageLimits.sort()
        left, right = 1, len(usageLimits)
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right


# Time:  O(nlogn)
# constructive algorithms, sort, binary search, greedy, prefix sum
class Solution4(object):
    def maxIncreasingGroups(self, usageLimits):
        def check(l):
            return all((i+1)*i//2 <= prefix[len(usageLimits)-(l-i)] for i in range(1, l+1))

        usageLimits.sort()
        prefix = [0]*(len(usageLimits)+1)
        for i in range(len(usageLimits)):
            prefix[i+1] = prefix[i]+usageLimits[i]
        left, right = 1, len(usageLimits)
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right
