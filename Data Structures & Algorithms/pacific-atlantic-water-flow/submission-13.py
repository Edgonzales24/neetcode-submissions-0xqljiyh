class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False] * COLS for i in range(ROWS)]
        atlantic = [[False] * COLS for i in range(ROWS)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[r][c] <= heights[nr][nc]):
                        q.append((nr, nc))


        pac, atl = [], []
        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS - 1))
        
        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS - 1, c))
        
        bfs(pac, pacific)
        bfs(atl, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if atlantic[r][c] and pacific[r][c]:
                    res.append((r, c))
        return res