# Time:  O(n)

class Solution(object):
    def minSwaps(self, data):
        
        total_count = sum(data)
        result, count, left = 0, 0, 0
        for i in range(len(data)):
            count += data[i]
            if i-left+1 > total_count: 
                count -= data[left]
                left += 1
            result = max(result, count)
        return total_count-result
