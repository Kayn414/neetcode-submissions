class Solution:

    def has_duplicates(self, lst):
        return len(lst) != len(set(lst))


    def get_box(self, matrix, b):
        box_row = b // 3
        box_col = b % 3
        start_row = box_row * 3
        start_col = box_col * 3

        box = []
        for i in range(3):
            for j in range(3):
                box.append(matrix[start_row + i][start_col + j])
        return box
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            row = [v for v in board[i] if v != "."]
            if self.has_duplicates(row):
                return False
        
        for j in range(n):
            col = [board[i][j] for i in range(n) if board[i][j] != "."]
            if self.has_duplicates(col):
                return False

        for b in range(9):
            box = self.get_box(board, b)
            filled = [v for v in box if v != "."]  
            if self.has_duplicates(filled):
                return False
        

        return True
        