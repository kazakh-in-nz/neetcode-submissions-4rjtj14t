class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        tr, tc = len(grid)-1, len(grid[0])-1
        rows, cols = len(grid), len(grid[0])
        
        visited = set()

        def dfs(r, c):
            if (min(r,c) < 0 or
            r >= rows or 
            c >=cols or
            grid[r][c] == 1 or 
            (r,c) in visited):
                return 0

            if r == tr and c == tc:
                return 1

            visited.add((r,c))

            res = 0
            res += dfs(r-1, c)
            res += dfs(r+1, c)
            res += dfs(r, c+1)
            res += dfs(r, c-1)

            visited.remove((r,c))
            return res

        return dfs(0, 0)