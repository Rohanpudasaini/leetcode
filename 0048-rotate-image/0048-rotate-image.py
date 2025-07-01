class Solution:

    def _transpose(self, matrix:List[List[int]], length:int) -> None:
        for i in range(length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        self._transpose(matrix, length)
        for i in range(length):
            matrix[i].reverse()



                
        