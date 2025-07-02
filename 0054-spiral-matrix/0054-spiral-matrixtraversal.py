class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        final_order = []

        def dfs(row, col, past_direction):
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            # Update the list to the have the most recently travelled direction first 
            directions.insert(0, directions.pop(directions.index(past_direction)))

            for direction in directions:
                n_row, n_col = row + direction[0], col + direction[1]

                # Check if new coordinate is inbounds, and we have't visisited it already
                if (n_row in range(len(matrix)) and
                    n_col in range(len(matrix[0])) and
                    (n_row, n_col) not in visited):
                    visited.add((n_row, n_col))
                    final_order.append(matrix[n_row][n_col])
                    dfs(n_row, n_col, direction)

        visited.add((0,0))
        final_order.append(matrix[0][0])
        dfs(0, 0, [0, 1])

        return final_order