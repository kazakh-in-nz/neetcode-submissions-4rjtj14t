from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r: int, c: int, visited: Set[Tuple[int, int]]):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()

                left = (r, c - 1)
                right = (r, c + 1)
                up = (r - 1, c)
                down = (r + 1, c)

                for r_new, c_new in [left, right, up, down]:
                    if (
                        r_new < 0 or r_new >= ROWS or 
                        c_new < 0 or c_new >= COLS or 
                        (r_new, c_new) in visited or
                        grid[r_new][c_new] == "0"
                    ):
                        continue

                    visited.add((r_new, c_new))
                    q.append((r_new, c_new))

        
        visited = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0" or (r, c) in visited:
                    continue

                res += 1
                bfs(r, c, visited)

        return res