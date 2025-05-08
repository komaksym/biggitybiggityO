# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        
        happiness.sort(reverse=True)
        return sum(max(happiness[i]-i, 0) for i in range(k))
