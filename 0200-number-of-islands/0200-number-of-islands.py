class Solution:
    def numIslands(self, grid):
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        # Boundary check or water
        if (i < 0 or j < 0 or
            i >= len(grid) or j >= len(grid[0]) or
            grid[i][j] == '0'):
            return

        # Mark as visited
        grid[i][j] = '0'

        # Down
        self.dfs(grid, i + 1, j)

        # Up
        self.dfs(grid, i - 1, j)

        # Right
        self.dfs(grid, i, j + 1)

        # Left
        self.dfs(grid, i, j - 1)