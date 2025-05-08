# Time:  O(n)

# combinatorics, number theory
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def exp_mod(p, mod):
            result = [p]
            while result[-1]*p%10 != result[0]:
                 result.append(result[-1]*p%10)
            return [result[-1]]+result[:-1]

        def inv_mod(x, mod):
            y = x
            while y*x%10 != 1:
                y = y*x%10
            return y

        def factor_p(x, p, cnt, diff):
            if x == 0:
                return x, cnt
            while x%p == 0:
                x //= p
                cnt += diff
            return x, cnt
    
        EXP = {p:exp_mod(p, 10) for p in (2, 5)} 
        INV = {i:inv_mod(i, 10) for i in range(1, 10) if i%2 and i%5} 
        result = 0
        nCr = 1
        cnt = {2:0, 5:0}
        for i in range(len(nums)):
            if not cnt[2] and not cnt[5]:
                result = (result + nCr*nums[i])%10
            elif cnt[2] and not cnt[5]:
                result = (result + nCr*EXP[2][cnt[2]%len(EXP[2])]*nums[i])%10
            elif not cnt[2] and cnt[5]:
                result = (result + nCr*EXP[5][cnt[5]%len(EXP[5])]*nums[i])%10
            mul, cnt[2] = factor_p((len(nums)-1)-i, 2, cnt[2], 1)
            mul, cnt[5] = factor_p(mul, 5, cnt[5], 1)
            div, cnt[2] = factor_p(i+1, 2, cnt[2], -1)
            div, cnt[5] = factor_p(div, 5, cnt[5], -1)
            nCr = nCr*mul%10
            nCr = nCr*INV[div%10]%10
        return result

# combinatorics
class Solution2(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nCr = 1
        for i in range(len(nums)):
            result = (result+nCr*nums[i])%10
            nCr *= (len(nums)-1)-i
            nCr //= i+1
        return result


# Time:  O(n^2)
# simulation
class Solution3(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in reversed(range(len(nums))):
            for j in range(i):
                nums[j] = (nums[j]+nums[j+1])%10
        return nums[0]
