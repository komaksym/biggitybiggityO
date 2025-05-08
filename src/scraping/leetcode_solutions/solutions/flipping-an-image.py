# Time:  O(n^2)


class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range((len(row)+1) // 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

