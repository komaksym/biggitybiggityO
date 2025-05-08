# Time:  O(nlogn)

class Solution(object):
    def findLongestChain(self, pairs):
        
        pairs.sort(key=lambda x: x[1])
        cnt, i = 0, 0
        for j in range(len(pairs)):
            if j == 0 or pairs[i][1] < pairs[j][0]:
                cnt += 1
                i = j
        return cnt

