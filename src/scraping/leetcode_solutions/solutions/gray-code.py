# Time:  O(2^n)

class Solution(object):
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            for n in reversed(result):
                result.append(1 << i | n)
        return result


# Proof of closed form formula could be found here:
# http://math.stackexchange.com/questions/425894/proof-of-closed-form-formula-to-convert-a-binary-number-to-its-gray-code
class Solution2(object):
    def grayCode(self, n):
        return [i >> 1 ^ i for i in range(1 << n)]


