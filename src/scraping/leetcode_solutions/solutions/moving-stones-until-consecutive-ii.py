# Time:  O(nlogn)

class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        left, min_moves = 0, float("inf")
        max_moves = max(stones[-1]-stones[1], stones[-2]-stones[0]) - (len(stones)-2)
        for right in range(len(stones)):
            while stones[right]-stones[left]+1 > len(stones):
                left += 1
            if len(stones)-(right-left+1) == 1 and stones[right]-stones[left]+1 == len(stones)-1:
                min_moves = min(min_moves, 2) 
            else:
                min_moves = min(min_moves, len(stones)-(right-left+1)) 
        return [min_moves, max_moves]
