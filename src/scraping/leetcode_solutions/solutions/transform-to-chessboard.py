# Time:  O(n^2)

import collections
import itertools


class Solution(object):
    def movesToChessboard(self, board):
        
        N = len(board)
        result = 0
        for count in (collections.Counter(list(map(tuple, board))), \
                      collections.Counter(zip(*board))):
            if len(count) != 2 or \
               sorted(count.values()) != [N/2, (N+1)/2]:
                return -1

            seq1, seq2 = count
            if any(x == y for x, y in zip(seq1, seq2)):
                return -1
            begins = [int(seq1.count(1) * 2 > N)] if N%2 else [0, 1]
            result += min(sum(int(i%2 != v) for i, v in enumerate(seq1, begin)) \
                          for begin in begins) / 2
        return result

