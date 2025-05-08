# Time:  O(m * n)

class Solution(object):
    def rotateTheBox(self, box):
        result = [['.']*len(box) for _ in range(len(box[0]))]
        for i in range(len(box)):
            k = len(box[0])-1
            for j in reversed(range(len(box[0]))):
                if box[i][j] == '.':
                    continue
                if box[i][j] == '*':
                    k = j
                result[k][-1-i] = box[i][j]
                k -= 1
        return result
