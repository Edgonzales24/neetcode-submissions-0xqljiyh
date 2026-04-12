class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            qLen = len(q)
            for i in range(qLen):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr in range(len(grid)) and
                        nc in range(len(grid[0])) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1