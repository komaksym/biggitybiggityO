# Time:  O(n)

# greedy
class Solution(object):
    def maxJump(self, stones):
        
        return stones[1]-stones[0] if len(stones) == 2 else max(stones[i+2]-stones[i] for i in range(len(stones)-2))
