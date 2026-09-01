class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions  = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS  or 
                        nc >= COLS or (nr,nc) in visited or grid[nr][nc] == 0):
                        continue
                    visited.add((nr, nc))
                    q.append((nr,nc))
                    area += 1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c))  
        
        return max_area

