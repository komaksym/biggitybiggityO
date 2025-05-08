from functools import reduce
# Time:  O(m * n + m * C(n, k))

# bitmasks, hakmem-175
class Solution(object):
    def maximumRows(self, matrix, numSelect):
        
        def next_popcount(n): 
            lowest_bit = n&-n
            left_bits = n+lowest_bit
            changed_bits = n^left_bits
            right_bits = (changed_bits//lowest_bit)>>2
            return left_bits|right_bits

        masks = [reduce(lambda m, c: m|(matrix[r][-1-c]<<c), range(len(matrix[0])), 0) for r in range(len(matrix))]
        result = 0
        mask = (1<<numSelect)-1
        while mask < 1<<len(matrix[0]):
            result = max(result, sum((m&mask) == m for m in masks))
            mask = next_popcount(mask)
        return result
