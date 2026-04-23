class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_occur = defaultdict(set)
        c_occur = defaultdict(set)
        sq_occur = defaultdict(set)

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                v = board[r][c]

                if v == ".":
                    continue

                sq = (r//3, c//3)

                if v in r_occur[r] or v in c_occur[c] or v in sq_occur[sq]:
                    return False

                r_occur[r].add(v)
                c_occur[c].add(v)
                sq_occur[sq].add(v)

        return True