# Time:  O(n)

# hash table, combinatorics
class Solution(object):
    def sumImbalanceNumbers(self, nums):
        right = [len(nums)]*len(nums)
        lookup = [len(nums)]*((len(nums)+1)+1)
        for i in reversed(range(len(nums))):
            right[i] = min(lookup[nums[i]], lookup[nums[i]+1]) 
            lookup[nums[i]] = i
        result = left = 0
        lookup = [-1]*((len(nums)+1)+1)
        for i in range(len(nums)):
            left = lookup[nums[i]+1]
            lookup[nums[i]] = i
            result += (i-left)*(right[i]-i)
        return result - (len(nums)+1)*len(nums)//2 


# Time:  O(n^2)
# hash table, two pointers
class Solution2(object):
    def sumImbalanceNumbers(self, nums):
        result = 0
        for right in range(len(nums)):
            lookup = {nums[right]}
            curr = 0
            for left in reversed(range(right)):
                if nums[left] not in lookup:
                    lookup.add(nums[left])
                    curr += 1-(nums[left]-1 in lookup)-(nums[left]+1 in lookup)
                result += curr
        return result
