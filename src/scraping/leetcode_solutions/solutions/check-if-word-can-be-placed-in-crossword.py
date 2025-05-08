# Time:  O(m * n)

class Solution(object):
    def placeWordInCrossword(self, board, word):
        
        def get_val(mat, i, j, transposed):
            return mat[i][j] if not transposed else mat[j][i]

        def get_vecs(mat, transposed):
            for i in range(len(mat) if not transposed else len(mat[0])):
                yield (get_val(mat, i, j, transposed) for j in range(len(mat[0]) if not transposed else len(mat)))

        for direction in (lambda x: iter(x), reversed):
            for transposed in range(2):
                for row in get_vecs(board, transposed):
                    it, matched = direction(word), True
                    for c in row:
                        if c == 
                            if next(it, None) is None and matched:
                                return True
                            it, matched = direction(word), True
                            continue
                        if not matched:
                            continue
                        nc = next(it, None)
                        matched = (nc is not None) and c in (nc, ' ')
                    if (next(it, None) is None) and matched:
                        return True
        return False


# Time:  O(m * n)
class Solution2(object):
    def placeWordInCrossword(self, board, word):
        
        words = [word, word[::-1]]
        for mat in (board, list(zip(*board))):
            for row in mat:
                blocks = ''.join(row).split(
                for s in blocks:
                    if len(s) != len(word):
                        continue
                    for w in words:
                        if all(s[i] in (w[i], ' ') for i in range(len(s))):
                            return True
        return False
