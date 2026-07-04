class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int, visited: Set[Tuple[int, int]]):
            if (
                (r, c) in visited or
                r >= ROWS or r < 0 or 
                c >= COLS or c < 0 or 
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))

            left = (r, c - 1)
            right = (r, c + 1)
            up = (r - 1, c)
            down = (r + 1, c)

            dfs(left[0], left[1], visited)
            dfs(right[0], right[1], visited)
            dfs(up[0], up[1], visited)
            dfs(down[0], down[1], visited)

        
        visited = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0" or (r, c) in visited:
                    continue

                res += 1
                dfs(r, c, visited)

        print(visited)

        return res


        