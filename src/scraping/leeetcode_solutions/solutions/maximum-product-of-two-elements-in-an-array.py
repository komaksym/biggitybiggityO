# Time:  O(n)

class Solution(object):
    def maxProduct(self, nums):
        
        m1 = m2 = 0
        for num in nums:
            if num > m1:
                m1, m2 = num, m1
            elif num > m2:
                m2 = num
        return (m1-1)*(m2-1)
