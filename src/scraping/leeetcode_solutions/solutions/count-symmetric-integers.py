# Time:  O(rlogr)

# brute force, memoization
MAX_R = 10**4
LOOKUP = [-1]*MAX_R
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        
        def check(x):
            if LOOKUP[x-1] == -1:
                digits = list(map(int, str(x)))
                if len(digits)%2:
                    LOOKUP[x-1] = 0
                else:
                    LOOKUP[x-1] = int(sum(digits[i] for i in range(len(digits)//2)) == sum(digits[i] for i in range(len(digits)//2, len(digits))))
            return LOOKUP[x-1]

        return sum(check(x) for x in range(low, high+1))
