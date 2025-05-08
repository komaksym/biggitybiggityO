# Time:  O((n + q) * logn)

# prefix sum, greedy, binary lifting
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        def ceil_log2_x(x):
            return (x-1).bit_length() if x-1 >= 0 else -1

        sorted_i = sorted((i for i in range(n)), key=lambda i : nums[i])
        i_to_idx = [0]*n
        for idx, i in enumerate(sorted_i):
            i_to_idx[i] = idx
        prefix = [0]*n
        for i in range(n-1):
            prefix[i+1] = prefix[i]+int(nums[sorted_i[i+1]]-nums[sorted_i[i]] > maxDiff)
        P = [[n-1]*n for _ in range(ceil_log2_x(n-1)+1)]
        left = 0
        for right in range(n):
            while nums[sorted_i[right]]-nums[sorted_i[left]] > maxDiff:
                P[0][left] = right-1
                left += 1
        for i in range(len(P)-1):
            for j in range(n):
                P[i+1][j] = P[i][P[i][j]]
        result = [-1]*len(queries)
        for idx, (i, j) in enumerate(queries):
            if i == j:
                result[idx] = 0
                continue
            if prefix[i_to_idx[i]] != prefix[i_to_idx[j]]:
                continue
            if i_to_idx[i] > i_to_idx[j]:
                i, j = j, i
            curr, l = i_to_idx[i], 0
            for k in reversed(range(len(P))):
                if P[k][curr] < i_to_idx[j]:
                    curr = P[k][curr]
                    l += 1<<k
            result[idx] = l+1
        return result
