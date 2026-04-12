class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = [[False] * COLS for i in range(ROWS)]
        atl = [[False] * COLS for i in range(ROWS)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                row, col = q.popleft()
                ocean[row][col] = True
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        heights[nr][nc] >= heights[row][col] and
                        not (ocean[nr][nc])):
                        q.append((nr, nc))
        
        pacific, atlantic = [], []
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res