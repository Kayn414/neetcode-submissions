class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            # bound checks
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]): # invalid path
                return False 
            
            temp = board[r][c]
            board[r][c] = '#' # visited pos

            exp = (dfs(r + 1, c, idx + 1) or # right
               dfs(r, c + 1, idx + 1) or # up 
                dfs(r - 1, c, idx + 1) or # left
                 dfs(r, c - 1, idx + 1)) # down

            board[r][c] = temp # clean visit

            return exp
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False