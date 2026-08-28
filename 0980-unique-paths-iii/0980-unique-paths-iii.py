class Solution:
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])

        total = 0
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] != -1:
                    total += 1
                if grid[r][c] == 1:
                    sr, sc = r, c

        def dfs(r, c, visited):
            if grid[r][c] == 2:
                return 1 if visited == total else 0

            original = grid[r][c]
            grid[r][c] = -1

            paths = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    paths += dfs(nr, nc, visited + 1)

            grid[r][c] = original
            return paths

        return dfs(sr, sc, 1)