# Time:  O(n)

# sliding window, two pointers
class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        
        result = curr = left = 0
        for right in range(len(colors)+k-1):  
            if right-left+1 == k:
                result += int(curr == k-1)
                curr -= int(colors[left] != colors[(left+1)%len(colors)])
                left += 1
            curr += int(colors[right%len(colors)] != colors[(right+1)%len(colors)])
        return result
