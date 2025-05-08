# Time:  O(n)

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        
        upper_matrix, lower_matrix = [0]*len(colsum), [0]*len(colsum)
        for i in range(len(colsum)):
            upper_matrix[i] = int(upper > 0 and colsum[i] != 0)
            lower_matrix[i] = colsum[i]-upper_matrix[i]
            upper -= upper_matrix[i]
            lower -= lower_matrix[i]
        return [upper_matrix, lower_matrix] if upper == lower == 0 else []
