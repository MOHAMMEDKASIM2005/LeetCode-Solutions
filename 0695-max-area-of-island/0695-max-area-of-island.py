class Solution:
    def maxAreaOfIsland(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        def dfs(row, col):

            # Outside the grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            # Water
            if grid[row][col] == 0:
                return 0

            # Mark as visited
            grid[row][col] = 0

            area = 1

            # Up
            area += dfs(row - 1, col)

            # Down
            area += dfs(row + 1, col)

            # Left
            area += dfs(row, col - 1)

            # Right
            area += dfs(row, col + 1)

            return area

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:

                    area = dfs(row, col)

                    max_area = max(max_area, area)

        return max_area
        