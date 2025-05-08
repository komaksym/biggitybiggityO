# Time:  O(n)

import collections


class Solution(object):
    def judgeCircle(self, moves):
        
        count = collections.Counter(moves)
        return count['L'] == count['R'] and count['U'] == count['D']

 
# Time:  O(n)
class Solution(object):
    def judgeCircle(self, moves):
        
        v, h = 0, 0
        for move in moves:
            if move == 'U':
                v += 1
            elif move == 'D':
                v -= 1
            elif move == 'R':
                h += 1
            elif move == 'L':
                h -= 1
        return v == 0 and h == 0
