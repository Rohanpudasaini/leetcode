class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from copy import deepcopy
        new_matrix = deepcopy(matrix)
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                matrix[j][length-1-i] = new_matrix[i][j]

                
        