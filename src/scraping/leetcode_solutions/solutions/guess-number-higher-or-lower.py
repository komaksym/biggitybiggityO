# Time:  O(logn)

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if guess(mid) <= 0: # noqa
                right = mid - 1
            else:
                left = mid + 1
        return left

