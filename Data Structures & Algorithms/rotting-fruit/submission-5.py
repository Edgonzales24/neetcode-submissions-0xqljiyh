class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh > 0:
            qLen = len(q)
            for i in range(qLen):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1