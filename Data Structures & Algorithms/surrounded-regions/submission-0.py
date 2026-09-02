class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        
        def bfs(r,c):
            q = deque([(r,c)])
            region = set([(r,c)])
            touches_edge = False

            while q:
                row, col = q.popleft()

                if (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1):
                    touches_edge = True
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and nc in range(COLS) and board[nr][nc] == "O" and (nr,nc) not in visit):
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        region.add((nr,nc))
            
            if not touches_edge:
                for r,c in region:
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visit:
                    visit.add((r,c))
                    bfs(r,c)
    