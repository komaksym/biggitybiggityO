# Time:  O(n)

# prefix sum
class Solution(object):
    def minimumLevels(self, possible):
        prefix = [0]*(len(possible)+1)
        for i in range(len(possible)):
            prefix[i+1] = prefix[i]+(+1 if possible[i] else -1)
        return next((i+1 for i in range(len(possible)-1) if prefix[i+1] > prefix[-1]-prefix[i+1]), -1)
