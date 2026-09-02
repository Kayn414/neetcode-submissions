class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        INF = 2147483647

        # Multi-source: enqueue all treasures (0s)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # changed from grid[r][c] == INF
                    q.append((r, c))

        # BFS from all treasures simultaneously
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    grid[nr][nc] == INF):  # unvisited empty land
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))



        


                
