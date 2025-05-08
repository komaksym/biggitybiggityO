# Time:  O(n)

# array
class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        result = float("-inf")
        for i in range(k):
            curr = 0
            for j in reversed(range(((len(energy)-i)-1)%k, len(energy)-i, k)): 
                curr += energy[j]
                result = max(result, curr)
        return result
