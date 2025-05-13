# Time:  O(n * logr)

# array
class Solution(object):
    def separateDigits(self, nums):
        result = []
        for x in reversed(nums):
            while x:
                result.append(x%10)
                x //= 10
        result.reverse()
        return result


# Time:  O(n * logr)
# array
class Solution2(object):
    def separateDigits(self, nums):
        return [int(c) for x in nums for c in str(x)]
