# Time:  O(n)

class Solution(object):
    def winnerOfGame(self, colors):
        
        cnt1 = cnt2 = 0
        for i in range(1, len(colors)-1):
            if not (colors[i-1] == colors[i] == colors[i+1]):
                continue
            if colors[i] == 'A':
                cnt1 += 1
            else:
                cnt2 += 1
        return cnt1 > cnt2
