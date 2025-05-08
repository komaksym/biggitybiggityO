# Time:  O(n)


class Solution(object):
    def largeGroupPositions(self, S):
        result = []
        i = 0
        for j in range(len(S)):
            if j == len(S)-1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    result.append([i, j])
                i = j+1
        return result

