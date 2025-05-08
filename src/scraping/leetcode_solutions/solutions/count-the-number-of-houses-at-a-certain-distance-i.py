# Time:  O(n)
# Space: O(1)

# math, prefix sum, difference array
class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        x, y = x-1, y-1
        if x > y:
            x, y = y, x
        diff = [0]*n
        for i in range(n):
            diff[0] += 1+1                                        
            diff[min(abs(i-x), abs(i-y)+1)] += 1                  
            diff[min(abs(i-y), abs(i-x)+1)] += 1                  
            diff[min(abs(i-0), abs(i-y)+1+abs(x-0))] -= 1         
            diff[min(abs(i-(n-1)), abs(i-x)+1+abs(y-(n-1)))] -= 1 
            diff[max(x-i, 0)+max(i-y, 0)+((y-x)+0)//2] -= 1       
            diff[max(x-i, 0)+max(i-y, 0)+((y-x)+1)//2] -= 1       
        for i in range(n-1):
            diff[i+1] += diff[i]
        return diff


# Time:  O(n^2)
# Space: O(1)
# math
class Solution2(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        x, y = x-1, y-1
        result = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                result[min(abs(i-j), abs(i-x)+1+abs(y-j), abs(i-y)+1+abs(x-j))-1] += 2
        return result
