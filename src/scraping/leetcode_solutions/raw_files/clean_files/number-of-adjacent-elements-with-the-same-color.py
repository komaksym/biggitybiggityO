# Time:  O(n + q)

# array
class Solution(object):
    def colorTheArray(self, n, queries):
        def update(i):
            if not nums[i]:
                return 0
            cnt = 0
            if i-1 >= 0 and nums[i-1] == nums[i]:
                cnt += 1
            if i+1 < n and nums[i+1] == nums[i]:
                cnt += 1
            return cnt

        nums = [0]*n
        result = [0]*len(queries)
        curr = 0
        for idx, (i, c) in enumerate(queries):
            curr -= update(i)
            nums[i] = c
            curr += update(i)
            result[idx] = curr
        return result
