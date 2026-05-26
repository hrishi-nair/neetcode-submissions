class Solution:
    def bfs(self, grid: List[List[str]], r: int, c: int):
        rows, cols = len(grid), len(grid[0])
        queue = deque([(r, c)])
        grid[r][c] = "0"  # Mark the starting piece as visited by sinking it
                
        while queue:
            row, col = queue.popleft()
                    
            # Check all 4 adjacent directions (Up, Down, Left, Right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                        
                # If the neighboring cell is within bounds and is land
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # We found a new island! Trigger BFS to clear it out.
                    island_count += 1
                    self.bfs(grid, r, c)
                    
        return island_count