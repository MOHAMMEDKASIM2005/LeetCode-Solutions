import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # min heap: (water_level_needed, row, col)
        minHeap = [(grid[0][0], 0, 0)]

        visited = set()

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Reached destination
            if r == n - 1 and c == n - 1:
                return time

            # 4 directions
            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    newTime = max(time, grid[nr][nc])

                    heapq.heappush(minHeap, (newTime, nr, nc))
        