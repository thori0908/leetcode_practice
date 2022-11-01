class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        result = True
        col_size = len(matrix[0])
        row_size = len(matrix)
        for row_i, current_row in enumerate(matrix):
            if col_size == 1: 
                break

            if row_i + 1 == row_size:
                break

            next_row = matrix[row_i+1]

            if current_row[0:col_size-1] != next_row[1:]:
                result = False
                break
        
        return result