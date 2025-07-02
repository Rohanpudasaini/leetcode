class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        result = []
        top = 0
        left =0
        right = column-1
        buttom = row-1
        while top <= buttom and left <=right:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, buttom+1):
                result.append(matrix[i][right])
            right -= 1
            if top <= buttom:
                for i in range(right, left-1, -1):
                    result.append(matrix[buttom][i])
                buttom -=1

            if left <=right:
                for i in range(buttom, top-1, -1):
                    result.append(matrix[i][left])
                left +=1


        return result
        