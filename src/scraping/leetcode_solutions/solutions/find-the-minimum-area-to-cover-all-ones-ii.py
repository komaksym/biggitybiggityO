# Time:  O(max(n, m)^2)

# dp
class Solution(object):
    def minimumSum(self, grid):
        def count(dir1, dir2):
            dp = [[0]*len(grid[0]) for _ in range(len(grid))]
            up = [len(grid)]*len(grid[0])
            down = [-1]*len(grid[0])
            for i in dir1(range(len(grid))):
                l, r, u, d = len(grid[0]), -1, len(grid), -1
                for j in dir2(range(len(grid[0]))):
                    if grid[i][j]:
                        up[j] = min(up[j], i)
                        down[j] = max(down[j], i)
                    u = min(u, up[j])
                    d = max(d, down[j])
                    if down[j] >= 0:
                        l = min(l, j)
                        r = max(r, j)
                    dp[i][j] = (r-l+1)*(d-u+1) if r >= 0 else 0
            return dp
        
        def count2(is_vertical):
            def get_n():
                return len(grid) if not is_vertical else len(grid[0])

            def get_m():
                return len(grid[0]) if not is_vertical else len(grid)

            def get(i, j):
                return grid[i][j] if not is_vertical else grid[j][i]
    
            left = [get_m() for _ in range(get_n())]
            right = [-1 for _ in range(get_n())]
            for i in range(get_n()):
                for j in range(get_m()):
                    if get(i, j) == 0:
                        continue
                    left[i] = min(left[i], j)
                    right[i] = max(right[i], j)
            dp = [[0]*get_n() for _ in range(get_n())]
            for i in range(len(dp)):
                l, r, u, d = get_m(), -1, get_n(), -1
                for j in range(i, len(dp[0])):
                    if right[j] != -1:
                        l = min(l, left[j])
                        r = max(r, right[j])
                        u = min(u, j)
                        d = max(d, j)
                    dp[i][j] = (r-l+1)*(d-u+1) if r >= 0 else 0
            return dp

        up_left = count(lambda x: x, lambda x: x)
        up_right = count(lambda x: x, reversed)
        down_left = count(reversed, lambda x: x)
        down_right = count(reversed, reversed)
        horizon = count2(False)
        vertical = count2(True)
        result = float("inf")
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                result = min(result,
                             up_left[i][j]+up_right[i][j+1]+horizon[i+1][len(grid)-1],
                             horizon[0][i]+down_left[i+1][j]+down_right[i+1][j+1],
                             up_left[i][j]+down_left[i+1][j]+vertical[j+1][len(grid[0])-1],
                             vertical[0][j]+up_right[i][j+1]+down_right[i+1][j+1])
        for i in range(len(grid)-2):
            for j in range(i+1, len(grid)-1):
                result = min(result, horizon[0][i]+horizon[i+1][j]+horizon[j+1][len(grid)-1])
        for i in range(len(grid[0])-2):
            for j in range(i+1, len(grid[0])-1):
                result = min(result, vertical[0][i]+vertical[i+1][j]+vertical[j+1][len(grid[0])-1])
        return result


# Time:  O(n * m * log(max(n, m)) + max(n, m)^2)
# sparse table
class Solution2(object):
    def minimumSum(self, grid):
        class SparseTable(object):
            def __init__(self, arr, fn):
                self.fn = fn
                self.bit_length = [0]
                n = len(arr)
                k = n.bit_length()-1  # log2_floor(n)
                for i in range(k+1):
                    self.bit_length.extend(i+1 for _ in range(min(1<<i, (n+1)-len(self.bit_length))))
                self.st = [[0]*n for _ in range(k+1)]
                self.st[0] = arr[:]
                for i in range(1, k+1):  # Time: O(NlogN) * O(fn)
                    for j in range((n-(1<<i))+1):
                        self.st[i][j] = fn(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])
        
            def query(self, L, R):  # Time: O(fn)
                i = self.bit_length[R-L+1]-1  # log2_floor(R-L+1)
                return self.fn(self.st[i][L], self.st[i][R-(1<<i)+1])

        def minimumArea(min_i, max_i, min_j, max_j):
            min_r = min(st_min_i[min_i].query(min_j, max_j), max_i+1)
            max_r = max(st_max_i[max_i].query(min_j, max_j), min_i-1)
            min_c = min(st_min_j[min_j].query(min_i, max_i), max_j+1)
            max_c = max(st_max_j[max_j].query(min_i, max_i), min_j-1)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0

        st_min_i = [None]*len(grid)
        curr = [len(grid)]*len(grid[0])
        for i in reversed(range(len(grid))):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    curr[j] = i
            st_min_i[i] = SparseTable(curr, min)
        st_max_i = [None]*len(grid)
        curr = [-1]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    curr[j] = i
            st_max_i[i] = SparseTable(curr, max)
        st_min_j = [None]*len(grid[0])
        curr = [len(grid[0])]*len(grid)
        for j in reversed(range(len(grid[0]))):
            for i in range(len(grid)):
                if grid[i][j]:
                    curr[i] = j
            st_min_j[j] = SparseTable(curr, min)
        st_max_j = [None]*len(grid[0])
        curr = [-1]*len(grid)
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j]:
                    curr[i] = j
            st_max_j[j] = SparseTable(curr, max)
        result = float("inf")
        for i in range(len(grid)-1):
            a = minimumArea(i+1, len(grid)-1, 0, len(grid[0])-1)
            for j in range(len(grid[0])-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(0, i, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid)-1):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in range(len(grid[0])-1):
                b = minimumArea(i+1, len(grid)-1, 0, j)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for j in range(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
            for i in range(len(grid)-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(i+1, len(grid)-1, 0, j)
                result = min(result, a+b+c)
        for j in range(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, 0, j)
            for i in range(len(grid)-1):
                b = minimumArea(0, i, j+1, len(grid[0])-1)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid)-2):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in range(i+1, len(grid)-1):
                b = minimumArea(i+1, j, 0, len(grid[0])-1)
                c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid[0])-2):
            a = minimumArea(0, len(grid)-1, 0, i)
            for j in range(i+1, len(grid[0])-1):
                b = minimumArea(0, len(grid)-1, i+1, j)
                c = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        return result


# Time:  O(n * m * log(max(n, m)) + max(n, m)^2)
# sparse table
class Solution3(object):
    def minimumSum(self, grid):
        class SparseTable(object):
            def __init__(self, arr, fn):
                self.fn = fn
                self.bit_length = [0]
                n = len(arr)
                k = n.bit_length()-1  # log2_floor(n)
                for i in range(k+1):
                    self.bit_length.extend(i+1 for _ in range(min(1<<i, (n+1)-len(self.bit_length))))
                self.st = [[0]*n for _ in range(k+1)]
                self.st[0] = arr[:]
                for i in range(1, k+1):  # Time: O(NlogN) * O(fn)
                    for j in range((n-(1<<i))+1):
                        self.st[i][j] = fn(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])
        
            def query(self, L, R):  # Time: O(fn)
                i = self.bit_length[R-L+1]-1  # log2_floor(R-L+1)
                return self.fn(self.st[i][L], self.st[i][R-(1<<i)+1])

        def minimumArea(min_i, max_i, min_j, max_j):
            min_r = min(st_min_i[min_i].query(min_j, max_j), max_i+1)
            max_r = max(st_max_i[max_i].query(min_j, max_j), min_i-1)
            min_c = min(st_min_j[min_j].query(min_i, max_i), max_j+1)
            max_c = max(st_max_j[max_j].query(min_i, max_i), min_j-1)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0

        result = float("inf")
        for _ in range(4):
            st_min_i = [None]*len(grid)
            curr = [len(grid)]*len(grid[0])
            for i in reversed(range(len(grid))):
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        curr[j] = i
                st_min_i[i] = SparseTable(curr, min)
            st_max_i = [None]*len(grid)
            curr = [-1]*len(grid[0])
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        curr[j] = i
                st_max_i[i] = SparseTable(curr, max)
            st_min_j = [None]*len(grid[0])
            curr = [len(grid[0])]*len(grid)
            for j in reversed(range(len(grid[0]))):
                for i in range(len(grid)):
                    if grid[i][j]:
                        curr[i] = j
                st_min_j[j] = SparseTable(curr, min)
            st_max_j = [None]*len(grid[0])
            curr = [-1]*len(grid)
            for j in range(len(grid[0])):
                for i in range(len(grid)):
                    if grid[i][j]:
                        curr[i] = j
                st_max_j[j] = SparseTable(curr, max)        
            for i in range(len(grid)-1):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(len(grid[0])-1):
                    b = minimumArea(i+1, len(grid)-1, 0, j)
                    c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                    result = min(result, a+b+c)
            for i in range(len(grid)-2):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(i+1, len(grid)-1):
                    b = minimumArea(i+1, j, 0, len(grid[0])-1)
                    c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                    result = min(result, a+b+c)
            grid = list(zip(*grid[::-1]))
        return result


# Time:  O(max(n, m)^2 * log(max(n, m)))
# prefix sum, binary search
class Solution4(object):
    def minimumSum(self, grid):
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
        
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def minimumArea(min_i, max_i, min_j, max_j):
            def count(x1, y1, x2, y2):
                cnt = grid[x2][y2]
                if x1-1 >= 0:
                    cnt -= grid[x1-1][y2]
                if y1-1 >= 0:
                    cnt -= grid[x2][y1-1]
                if x1-1 >= 0 and y1-1 >= 0:
                    cnt += grid[x1-1][y1-1]
                return cnt

            min_r = binary_search(min_i, max_i, lambda i: count(min_i, min_j, i, max_j))
            max_r = binary_search_right(min_i, max_i, lambda i: count(i, min_j, max_i, max_j))
            min_c = binary_search(min_j, max_j, lambda j: count(min_i, min_j, max_i, j))
            max_c = binary_search_right(min_j, max_j, lambda j: count(min_i, j, max_i, max_j))
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
                if j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    grid[i][j] -= grid[i-1][j-1]
        result = float("inf")
        result = float("inf")
        for i in range(len(grid)-1):
            a = minimumArea(i+1, len(grid)-1, 0, len(grid[0])-1)
            for j in range(len(grid[0])-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(0, i, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid)-1):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in range(len(grid[0])-1):
                b = minimumArea(i+1, len(grid)-1, 0, j)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for j in range(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
            for i in range(len(grid)-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(i+1, len(grid)-1, 0, j)
                result = min(result, a+b+c)
        for j in range(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, 0, j)
            for i in range(len(grid)-1):
                b = minimumArea(0, i, j+1, len(grid[0])-1)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid)-2):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in range(i+1, len(grid)-1):
                b = minimumArea(i+1, j, 0, len(grid[0])-1)
                c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid[0])-2):
            a = minimumArea(0, len(grid)-1, 0, i)
            for j in range(i+1, len(grid[0])-1):
                b = minimumArea(0, len(grid)-1, i+1, j)
                c = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        return result


# Time:  O(max(n, m)^2 * log(max(n, m)))
# prefix sum, binary search
class Solution5(object):
    def minimumSum(self, grid):
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
        
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def minimumArea(min_i, max_i, min_j, max_j):
            def count(x1, y1, x2, y2):
                cnt = prefix[x2][y2]
                if x1-1 >= 0:
                    cnt -= prefix[x1-1][y2]
                if y1-1 >= 0:
                    cnt -= prefix[x2][y1-1]
                if x1-1 >= 0 and y1-1 >= 0:
                    cnt += prefix[x1-1][y1-1]
                return cnt

            min_r = binary_search(min_i, max_i, lambda i: count(min_i, min_j, i, max_j))
            max_r = binary_search_right(min_i, max_i, lambda i: count(i, min_j, max_i, max_j))
            min_c = binary_search(min_j, max_j, lambda j: count(min_i, min_j, max_i, j))
            max_c = binary_search_right(min_j, max_j, lambda j: count(min_i, j, max_i, max_j))
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for _ in range(4):
            prefix = [[0]*len(grid[0]) for _ in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    prefix[i][j] = grid[i][j]
                    if i-1 >= 0:
                        prefix[i][j] += prefix[i-1][j]
                    if j-1 >= 0:
                        prefix[i][j] += prefix[i][j-1]
                    if i-1 >= 0 and j-1 >= 0:
                        prefix[i][j] -= prefix[i-1][j-1]
            for i in range(len(grid)-1):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(len(grid[0])-1):
                    b = minimumArea(i+1, len(grid)-1, 0, j)
                    c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                    result = min(result, a+b+c)
            for i in range(len(grid)-2):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(i+1, len(grid)-1):
                    b = minimumArea(i+1, j, 0, len(grid[0])-1)
                    c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                    result = min(result, a+b+c)
            grid = list(zip(*grid[::-1]))
        return result


# Time:  O((n^2 + m^2 + 4 * n * m) * n * m) = O(max(n, m)^3 * min(n, m))
# brute force
class Solution6(object):
    def minimumSum(self, grid):
        def minimumArea(min_i, max_i, min_j, max_j):
            min_r, max_r, min_c, max_c = max_i+1, min_i-1, max_j+1, min_j-1
            for i in range(min_i, max_i+1):
                for j in range(min_j, max_j+1):
                    if grid[i][j] == 0:
                        continue
                    min_r, max_r, min_c, max_c = min(min_r, i), max(max_r, i), min(min_c, j), max(max_c, j)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for i in range(len(grid)-1):
            a = minimumArea(i+1, len(grid)-1, 0, len(grid[0])-1)
            for j in range(len(grid[0])-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(0, i, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid)-1):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in range(len(grid[0])-1):
                b = minimumArea(i+1, len(grid)-1, 0, j)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for j in range(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
            for i in range(len(grid)-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(i+1, len(grid)-1, 0, j)
                result = min(result, a+b+c)
        for j in range(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, 0, j)
            for i in range(len(grid)-1):
                b = minimumArea(0, i, j+1, len(grid[0])-1)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid)-2):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in range(i+1, len(grid)-1):
                b = minimumArea(i+1, j, 0, len(grid[0])-1)
                c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in range(len(grid[0])-2):
            a = minimumArea(0, len(grid)-1, 0, i)
            for j in range(i+1, len(grid[0])-1):
                b = minimumArea(0, len(grid)-1, i+1, j)
                c = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        return result


# Time:  O((n^2 + m^2 + 4 * n * m) * n * m) = O(max(n, m)^3 * min(n, m))
# brute force
class Solution7(object):
    def minimumSum(self, grid):
        def minimumArea(min_i, max_i, min_j, max_j):
            min_r, max_r, min_c, max_c = max_i+1, min_i-1, max_j+1, min_j-1
            for i in range(min_i, max_i+1):
                for j in range(min_j, max_j+1):
                    if grid[i][j] == 0:
                        continue
                    min_r, max_r, min_c, max_c = min(min_r, i), max(max_r, i), min(min_c, j), max(max_c, j)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for _ in range(4):
            for i in range(len(grid)-1):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(len(grid[0])-1):
                    b = minimumArea(i+1, len(grid)-1, 0, j)
                    c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                    result = min(result, a+b+c)
            for i in range(len(grid)-2):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(i+1, len(grid)-1):
                    b = minimumArea(i+1, j, 0, len(grid[0])-1)
                    c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                    result = min(result, a+b+c)
            grid = list(zip(*grid[::-1]))
        return result
