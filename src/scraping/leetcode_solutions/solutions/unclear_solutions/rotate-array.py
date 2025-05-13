# Time:  O(n)

class Solution(object):
    def rotate(self, nums, k):
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end - 1] = nums[end - 1], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))


# Time:  O(n)
from fractions import gcd


class Solution2(object):
    def rotate(self, nums, k):
        def apply_cycle_permutation(k, offset, cycle_len, nums):
            tmp = nums[offset]
            for i in range(1, cycle_len):
                nums[(offset + i * k) % len(nums)], tmp = tmp, nums[(offset + i * k) % len(nums)]
            nums[offset] = tmp

        k %= len(nums)
        num_cycles = gcd(len(nums), k)
        cycle_len = len(nums) / num_cycles
        for i in range(num_cycles):
            apply_cycle_permutation(k, i, cycle_len, nums)


# Time:  O(n)
class Solution3(object):
    def rotate(self, nums, k):
        count = 0
        start = 0
        while count < len(nums):
            curr = start
            prev = nums[curr]
            while True:
                idx = (curr + k) % len(nums)
                nums[idx], prev = prev, nums[idx]
                curr = idx
                count += 1
                if start == curr:
                    break
            start += 1


# Time:  O(n)
class Solution4(object):
    def rotate(self, nums, k):
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
class Solution5(object):
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

 
