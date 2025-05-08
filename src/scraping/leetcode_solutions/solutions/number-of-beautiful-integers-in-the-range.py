# Time:  O(n^2 * k), n = len(str(high))

# memoization (faster but more space)
class Solution(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        TIGHT, UNTIGHT, UNBOUND = list(range(3))
        def f(x):
            digits = list(map(int, str(x)))
            lookup = [[[[-1]*k for _ in range(2*len(digits)+1)] for _ in range(3)] for _ in range(len(digits))]
            def memoization(i, state, diff, total):
                if i == len(digits):
                    return int(state != UNBOUND and diff == total == 0)
                if lookup[i][state][diff][total] == -1:
                    result = int(i != 0 and diff == total == 0)  # count if the beautiful integer x s.t. len(str(x)) < len(digits)
                    for d in range(1 if i == 0 else 0, 10):
                        new_state = state
                        if state == TIGHT and d != digits[i]:
                            new_state = UNTIGHT if d < digits[i] else UNBOUND
                        new_diff = diff+(1 if d%2 == 0 else -1)
                        new_total = (total*10+d)%k
                        result += memoization(i+1, new_state, new_diff, new_total)
                    lookup[i][state][diff][total] = result
                return lookup[i][state][diff][total]
    
            return memoization(0, TIGHT, 0, 0)

        return f(high)-f(low-1)


# Time:  O(n^2 * k), n = len(str(high))
# dp (slower but less space)
class Solution2(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        TIGHT, UNTIGHT, UNBOUND = list(range(3))
        def f(x):
            digits = list(map(int, str(x)))
            dp = [[[0]*k for _ in range(2*len(digits)+1)] for _ in range(3)]
            for tight in range(2):
                for state in (TIGHT, UNTIGHT):
                    dp[state][0][0] = 1
            for i in reversed(range(len(digits))):
                new_dp = [[[0]*k for _ in range(2*len(digits)+1)] for _ in range(3)]
                for state in (TIGHT, UNTIGHT, UNBOUND):
                    new_dp[state][0][0] = int(i != 0)  # count if the beautiful integer x s.t. len(str(x)) < len(digits)
                    for d in range(1 if i == 0 else 0, 10):
                        new_state = state
                        if state == TIGHT and d != digits[i]:
                            new_state = UNTIGHT if d < digits[i] else UNBOUND
                        for diff in range(-len(digits), len(digits)+1):
                            new_diff = diff+(1 if d%2 == 0 else -1)
                            for total in range(k):
                                new_total = (total*10+d)%k
                                new_dp[state][diff][total] += dp[new_state][new_diff][new_total]
                dp = new_dp
            return dp[TIGHT][0][0]

        return f(high)-f(low-1)


# Time:  O(n^2 * k), n = len(str(high))
# memoization (faster but more space)
class Solution3(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        def f(x):
            digits = list(map(int, str(x)))
            lookup = [[[[[-1]*k for _ in range(2*len(digits)+1)] for _ in range(2)] for _ in range(2)] for _ in range(len(digits))]
            def memoization(i, zero, tight, diff, total):
                if i == len(digits):
                    return int(zero == diff == total == 0)
                if lookup[i][zero][tight][diff][total] == -1:
                    result = 0
                    for d in range((digits[i] if tight else 9)+1):
                        new_zero = int(zero and d == 0)
                        new_tight = int(tight and d == digits[i])
                        new_diff = diff+((1 if d%2 == 0 else -1) if new_zero == 0 else 0)
                        new_total = (total*10+d)%k
                        result += memoization(i+1, new_zero, new_tight, new_diff, new_total)
                    lookup[i][zero][tight][diff][total] = result
                return lookup[i][zero][tight][diff][total]
    
            return memoization(0, 1, 1, 0, 0)

        return f(high)-f(low-1)


# Time:  O(n^2 * k), n = len(str(high))
# dp (slower but less space)
class Solution4(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        def f(x):
            digits = list(map(int, str(x)))
            dp = [[[[0]*k for _ in range(2*len(digits)+1)] for _ in range(2)] for _ in range(2)]
            for tight in range(2):
                dp[0][tight][0][0] = 1
            for i in reversed(range(len(digits))):
                new_dp = [[[[0]*k for _ in range(2*len(digits)+1)] for _ in range(2)] for _ in range(2)]
                for zero in range(2):
                    for tight in range(2):
                        for d in range((digits[i] if tight else 9)+1):
                            new_zero = int(zero and d == 0)
                            new_tight = int(tight and d == digits[i])
                            for diff in range(-len(digits), len(digits)+1):
                                new_diff = diff+((1 if d%2 == 0 else -1) if new_zero == 0 else 0)
                                for total in range(k):
                                    new_total = (total*10+d)%k
                                    new_dp[zero][tight][diff][total] += dp[new_zero][new_tight][new_diff][new_total]
                dp = new_dp
            return dp[1][1][0][0]

        return f(high)-f(low-1)
