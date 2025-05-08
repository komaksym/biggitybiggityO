# Time:  O(n)

# array
class Solution(object):
    def maximumEnergy(self, energy, k):
        
        result = float("-inf")
        for i in range(k):
            curr = 0
            for j in reversed(range(((len(energy)-i)-1)%k, len(energy)-i, k)): 
                curr += energy[j]
                result = max(result, curr)
        return result
