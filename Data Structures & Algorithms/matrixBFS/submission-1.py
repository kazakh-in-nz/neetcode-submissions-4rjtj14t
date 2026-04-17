from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        tr, tc = rows-1, cols-1
        visited = set()

        if grid[0][0] == 1:
            return -1

        q = deque()
        q.append((0, 0, 0))

        while len(q) > 0:
            nr, nc, dist = q.popleft()

            if nr == tr and nc == tc:
                return dist

            directions = [(nr+1, nc), (nr-1, nc), (nr, nc+1), (nr, nc-1)]

            for dr, dc in directions:
                if (
                    min(dr,dc) < 0 or
                    dr >= rows or
                    dc >= cols or
                    (dr, dc) in visited or
                    grid[dr][dc] == 1
                ):
                    continue

                q.append((dr, dc, dist+1))
                visited.add((dr, dc))

        return -1

