# Time:  O(n)

# bit manipulation
class Solution(object):
    def subsequenceSumOr(self, nums):
        result = prefix = 0
        for x in nums:
            prefix += x
            result |= x|prefix
        return result


# Time:  O(nlogn)
# bit manipulation
class Solution2(object):
    def subsequenceSumOr(self, nums):
        result = cnt = 0
        for i in range(64):
            cnt >>= 1
            for x in nums:
                cnt += (x>>i)&1
            if cnt:
                result |= 1<<i
        return result
