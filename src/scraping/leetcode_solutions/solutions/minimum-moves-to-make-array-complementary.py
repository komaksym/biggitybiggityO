# Time:  O(n + k)

class Solution(object):
    def minMoves(self, nums, limit):
        diff = [0]*(2*(limit+1))
        for i in range(len(nums)//2):
            left, right = nums[i], nums[-1-i]
            diff[min(left, right)+1] -= 1       
            diff[left+right] -= 1               
            diff[left+right+1] += 1             
            diff[max(left, right)+limit+1] += 1 
        result = count = len(nums)              
        for total in range(2, 2*limit+1):      
            count += diff[total]
            result = min(result, count)
        return result
