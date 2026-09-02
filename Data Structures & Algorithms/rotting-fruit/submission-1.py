class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0
        fresh = 0
        q = deque()

        for r in range(ROWS):
          for c in range(COLS):
              if grid[r][c] == 1:
                  fresh += 1
              if grid[r][c] == 2:
                  q.append((r,c))

    
        while fresh > 0 and q:
            level_size = len(q)
            for _ in range(level_size):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                        and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        
      