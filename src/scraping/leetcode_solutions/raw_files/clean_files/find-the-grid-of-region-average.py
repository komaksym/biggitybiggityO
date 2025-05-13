# Time:  O(m * n)

# array
class Solution(object):
    def resultGrid(self, image, threshold):
        def check(i, j):
            return (all(abs(image[ni][nj]-image[ni+1][nj]) <= threshold for ni in range(i-1, i+1) for nj in range(j-1, j+2)) and
                    all(abs(image[ni][nj]-image[ni][nj+1]) <= threshold for ni in range(i-1, i+2) for nj in range(j-1, j+1)))
            
        result = [[0]*len(image[0]) for _ in range(len(image))]
        cnt = [[0]*len(image[0]) for _ in range(len(image))]
        for i in range(1, len(image)-1):
            for j in range(1, len(image[0])-1):
                if not check(i, j):
                    continue
                total = sum(image[ni][nj] for ni in range(i-1, i+2) for nj in range(j-1, j+2))//9
                for ni in range(i-1, i+2):
                    for nj in range(j-1, j+2):
                        cnt[ni][nj] += 1
                        result[ni][nj] += total
        for i in range(len(image)):
            for j in range(len(image[0])):
                if cnt[i][j]:
                    result[i][j] //= cnt[i][j]
                else:
                    result[i][j] = image[i][j]
        return result
