class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ROW , COL = len(board), len(board[0])
        solutions = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                solutions.append(copy)
                return
            for c in range(n):
                if self.is_safe(board, r, c, n):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
        backtrack(0)
        return solutions
                    

    def is_safe(self, board, rows, cols, n):
        for i in range(rows):
            if board[i][cols] == "Q":
                return False

        for i in range(cols):
            if board[rows][i] == "Q":
                return False

        row, col = rows - 1, cols - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -=1

        
        row, col = rows - 1, cols + 1
        while row >= 0 and col < n:
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True


