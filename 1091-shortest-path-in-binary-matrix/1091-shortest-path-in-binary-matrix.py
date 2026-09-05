from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue = deque()
        queue.append((0, 0, 1))

        visited = set()
        visited.add((0, 0))

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        while queue:

            r, c, distance = queue.popleft()

            if r == n-1 and c == n-1:
                return distance

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        
                        visited.add((nr, nc))
                        
                        queue.append(
                            (nr, nc, distance + 1)
                        )

        return -1