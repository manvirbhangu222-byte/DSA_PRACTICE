from collections import deque

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1

                    queue = deque([(r, c)])
                    grid[r][c] = "0"

                    while queue:
                        current_r, current_c = queue.popleft()

                        for dr, dc in directions:
                            nr = current_r + dr
                            nc = current_c + dc

                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and grid[nr][nc] == "1"
                            ):
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))

        return islands