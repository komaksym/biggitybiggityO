# Time:  O(n)

class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        result = 0
        for c1 in [1, -1]:
            for c2 in [1, -1]:
                min_prev = float("inf")
                for i in range(len(arr1)):
                    curr = c1*arr1[i] + c2*arr2[i] + i
                    result = max(result, curr-min_prev)
                    min_prev = min(min_prev, curr)
        return result

class Solution2(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        return max(max(c1*arr1[i] + c2*arr2[i] + i for i in range(len(arr1))) -
                   min(c1*arr1[i] + c2*arr2[i] + i for i in range(len(arr1)))
                   for c1 in [1, -1] for c2 in [1, -1])
