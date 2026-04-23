class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = {}
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                v = board[r][c]
                
                if v == ".":
                    continue 

                sq = (r//3, c//3)

                if v not in m:
                    m[v] = [(r, c, sq)]
                else:
                    i = 0

                    print(v)

                    while i < len(m[v]):
                        tr, tc, tsq = m[v][i]

                        if tr == r or tc == c or (tsq[0] == sq[0] and tsq[1] == sq[1]):
                            return False

                        i += 1

                    m[v].append((r, c, sq))
        
        return True

        