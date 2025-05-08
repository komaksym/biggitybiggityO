# Time:  O(m * n)

class Solution(object):
    def findFarmland(self, land):
        
        result = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] != 1:
                    continue
                ni, nj = i, j
                while ni+1 < len(land) and land[ni+1][j] == 1:
                    ni += 1
                while nj+1 < len(land[0]) and land[i][nj+1] == 1:
                    nj += 1
                for r in range(i, ni+1):
                    for c in range(j, nj+1):
                        land[r][c] = -1
                result.append([i, j, ni, nj])
        return result
